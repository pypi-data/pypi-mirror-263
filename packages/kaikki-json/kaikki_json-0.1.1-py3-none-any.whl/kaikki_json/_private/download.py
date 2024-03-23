

import os

import requests

from .config import config


def download_kaikki(force=False, verbose=True) -> None:
    def log(*args, **kwargs) -> None:
        if verbose:
            print(*args, **kwargs)

    file_path = config.gz_file_path

    if not force and os.path.exists(file_path):
        log('File already downloaded.')
        return

    os.makedirs(os.path.dirname(file_path), exist_ok=True)
    response = requests.get('https://kaikki.org/dictionary/raw-wiktextract-data.json.gz', stream=True)
    log(f'Downloading file to {file_path} ...')
    if response.ok:
        try:
            content_length = int(response.headers['Content-Length'])
            log(f'Size: {content_length / (2 ** 30):.2f}GB')
        except:
            content_length = 0
        bytes_read = 0
        next_landmark = 0
        log()
        with open(file_path, 'wb') as file:
            for chunk in response.iter_content(chunk_size=config.chunk_size):
                if content_length > 0:
                    progress = int(100.0 * bytes_read / content_length)
                    if progress >= next_landmark:
                        log(f'\33[F\33[2K > {progress}% ...')
                        next_landmark = progress + 1
                if chunk:
                    file.write(chunk)
                    bytes_read += len(chunk)
        log('Done.')
    else:
        raise Exception(f'Download failed: status code {response.status_code}\n{response.text}')
