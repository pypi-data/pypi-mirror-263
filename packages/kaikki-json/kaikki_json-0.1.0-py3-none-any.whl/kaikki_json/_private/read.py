

import gzip
from json import loads
from typing import Any, Iterable

from .config import config


def iter_texts() -> Iterable[str]:
    try:
        with gzip.open(config.gz_file_path, 'rt', encoding='utf8') as file:
            yield from file
    except FileNotFoundError as e:
        raise Exception('Data not found. Maybe it needs to be downloaded: `python -m kaikki_json --download`') from e


def iter_items() -> Iterable[Any]:
    return map(loads, iter_texts())


def iter_items_in(lang_code: str) -> Iterable[Any]:
    needle = f'"{lang_code}"'
    for text in iter_texts():
        if needle not in text:
            continue
        item = loads(text)
        if item.get('lang_code', None) != lang_code:
            continue
        yield item
