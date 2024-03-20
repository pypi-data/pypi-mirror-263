import requests
import os
import traceback
import concurrent.futures
from urllib.parse import urlparse
from urllib.parse import parse_qs
import argparse
import shelve
import time
from threading import Event
import logging
event = Event()
logger = logging.getLogger(__name__)

UPLOAD_CHUNK_SIZE = 1024 * 1024 * 1024  # 1gb
MAX_RETRY_ALLOWED = 2
OK_STATUS = [200, 201]
# Initialize the file where the result of cached methods will be stored.
cache_file = 'cache.nowgg'
cache = shelve.open(cache_file, writeback=True)

max_retry_map = {}


def get_host():
    return cache.get("host", "https://api-studio.now.gg")


def perform_upload(file_path, start_byte, end_byte, presigned_url, part_num):
    if event.is_set():
        return None
    with open(file_path, 'rb') as file:
        file.seek(start_byte)
        chunk = file.read(end_byte - start_byte)

        response = requests.put(presigned_url, data=chunk)
        logger.debug(f"Uploaded Part: {part_num}")
        response.raise_for_status()
        return response


def upload_part(file_path, start_byte, end_byte, presigned_url, partNum):
    
    while (max_retry_map[partNum] >= 0):
        if event.is_set():
            return None
        try:
            return perform_upload(file_path, start_byte, end_byte, presigned_url, partNum)
        except Exception as e:
            logger.error(f"Error uploading part {partNum}: {e}")
        max_retry_map[partNum] = max_retry_map[partNum] - 1
        if max_retry_map[partNum] < 0:
            break
        time.sleep(1)
    return None        

def upload_async(file_path, part_id_url_list, chunks_count):
    promises_array = []
    with concurrent.futures.ThreadPoolExecutor(5) as executor:
        futures = []
    
        for current_part in range(1, chunks_count + 1):
            max_retry_map[current_part] = MAX_RETRY_ALLOWED
            current_chunk_start_byte = (current_part - 1) * UPLOAD_CHUNK_SIZE
            current_chunk_end_byte = current_part * UPLOAD_CHUNK_SIZE
            presigned_url = part_id_url_list[current_part - 1]
            future = executor.submit(
                upload_part, file_path, current_chunk_start_byte, current_chunk_end_byte, presigned_url, current_part)
            futures.append(future)
        logger.info("Starting upload..")
        for completed_future in concurrent.futures.as_completed(futures):
            if event.is_set():
                executor.shutdown(wait=False)
                break
            progress = (
                len([f for f in futures if f.done()]) / chunks_count) * 100
            logger.info(f"Uploading... {progress:.2f}%")

            response = completed_future.result()
            if response:
                promises_array.append(response)
            else:
                event.set()
                logger.error("Error occurred during part upload.")
    if event.is_set():
        return []                 
    return promises_array


def upload_file(file_path, game_id, token, app_version, app_version_code):
    try:
        file_name = os.path.basename(file_path)
        upload_type = "upload_file_zip" if file_name.endswith(".zip") or file_name.endswith(
            ".rar") or file_name.endswith(".7z") else "upload_file"
        headers = {"publisher_token": token}

        file_size = os.path.getsize(file_path)
        chunks_count = int((file_size // UPLOAD_CHUNK_SIZE) + 1)

        # Initialize multipart upload
        response = requests.post(f"{get_host()}/v2/publisher/asset/mutipart_upload/start",
                                    params={"file_name": file_name, "game_id": game_id,
                                            "parts_count": chunks_count},
                                    headers=headers)
        
        if response.status_code not in OK_STATUS:
            logger.error(response.json().get('message', response.reason))
            return                           
        data = response.json().get('data', {})
        upload_id = data.get('upload_id', "")
        part_id_url_list = data.get('presigned_url_data')
        s3_file_path = data.get('s3_file_path')
         
        promises_array = upload_async(
            file_path, part_id_url_list, chunks_count)
        
        if not promises_array:
            logger.error("Error while uploading file. Please try again after some time.")
            return

        upload_parts_array = []
        for i, resp in enumerate(promises_array):
            parsed_url = urlparse(resp.url)
            part_num = parse_qs(parsed_url.query)['partNumber'][0]
            upload_parts_array.append(
                {"ETag": resp.headers['ETag'].replace('"', ''), "PartNumber": int(part_num)})

        sorted_upload_parts_array = sorted(
            upload_parts_array, key=lambda x: x['PartNumber'])
        response = requests.post(f"{get_host()}/v2/publisher/asset/mutipart_upload/end", json={
                                    "upload_id": upload_id, "parts_info": sorted_upload_parts_array,
                                    "s3_file_path": s3_file_path}, headers=headers)
        response.raise_for_status
        if response.status_code in OK_STATUS:
            logger.info("Upload completed.")
            file_url = f"https://cdn.now.gg/{s3_file_path}"
            response = requests.post(
                f"{get_host()}/v2/publisher/apk-library",
                json={"upload_url": file_url,
                        "app_version": app_version,
                        "app_version_code": app_version_code,
                        "game_id": game_id,
                        "upload_type": upload_type}, headers=headers)
            if response.status_code in OK_STATUS:
                logger.info("Successfully uploaded to your Apk Library!")
            else:
                logger.debug(response.reason)
        else:
            logger.error(response.json().get('message', response.reason))

    except Exception as e:
        traceback.print_exc()
        logger.error(f"Error: {e}")


class Nowgg:

    def config(self, hostname=""):
        
        if hostname:
            old_host = get_host()
            cache["host"] = hostname
            logger.info(f"changed host from {old_host} to {hostname}")
        else:
            logger.info(get_host()) 

    def init(self, token):
        """Init
        Args:
            token (str): required parameter token
        """

        cache['token'] = token
        logger.info("init successful!")

    def upload(self, app_id, app_file_path, app_version, app_version_code):
        """Upload utility

        Args:
            app_id (str): required parameter app_id
            app_file_path (str): required parameter app_file_path
            app_version (str): required parameter app_version
            app_version_code (int): required parameter app_version_code

        """
        token = cache.get('token')
        if token:
            return upload_file(app_file_path, app_id, token, app_version, app_version_code)
        else:
            logger.error("Please init first with token. nowgg init -t <your-token>")


def main():
    
    logger.setLevel(logging.INFO)
    nowgg = Nowgg()
    parser = argparse.ArgumentParser(description="nowgg: Nowgg CLI")
    parser.add_argument("-v", "--verbose", help="increase output verbosity",
                    action="store_true")

    subparsers = parser.add_subparsers(
        title='subcommands', dest='command', description='Choose one of the following operations')

    # Subparser for the init command
    init_parser = subparsers.add_parser('init', help='Init', formatter_class=fmt)
    init_parser.add_argument('-t', '--token', type=str, help='Publisher Token', required=True)

    # Subparser for the upload command
    upload_parser = subparsers.add_parser('upload', help='Upload utility', formatter_class=fmt)
    upload_parser.add_argument(
        '-a', '--app_id', type=str, help='App Id', required=True)
    upload_parser.add_argument(
        '-f', '--file_path', type=str, help='File Path', required=True)
    upload_parser.add_argument(
        '-av', '--apk_version', type=str, help='apk version name', required=True)
    upload_parser.add_argument(
        '-vc', '--version_code', type=int, help='apk version code', required=True)

    config_parser = subparsers.add_parser('config')
    config_parser.add_argument('-hn', '--host_name', help=argparse.SUPPRESS, required=False)

    args = parser.parse_args()
    if args.verbose:
        logger.setLevel(logging.DEBUG)

    if args.command == 'init':
        nowgg.init(args.token)
    elif args.command == 'upload':
        nowgg.upload(args.app_id, args.file_path,
                     args.apk_version, args.version_code)
    elif args.command == 'config':
        nowgg.config(args.host_name)   
    else:
        parser.print_help()


class CustomHelpFormatter(argparse.HelpFormatter):
    def _format_action_invocation(self, action):
        if not action.option_strings or action.nargs == 0:
            return super()._format_action_invocation(action)
        # default = self._get_default_metavar_for_optional(action)
        args_string = self._format_args(action, '')
        return ', '.join(action.option_strings) + ' ' + args_string


fmt = lambda prog: CustomHelpFormatter(prog)


if __name__ == "__main__":
    main()
