
import os
from dataclasses import dataclass

from appdirs import user_cache_dir


@dataclass
class Config:
    package_name: str = 'kaikki_json'
    file_name: str = 'kaikki.json.gz'
    download_url: str = 'https://kaikki.org/dictionary/raw-wiktextract-data.json.gz'
    chunk_size: int = 2 ** 20

    @property
    def cache_dir(self) -> str:
        return str(user_cache_dir(self.package_name))

    @property
    def gz_file_path(self) -> str:
        return os.path.join(self.cache_dir, self.file_name)

    def __str__(self) -> str:
        lines: list[str] = []
        for key in dir(self):
            if key.startswith('_'):
                continue
            lines.append(f'{key}: {getattr(self, key)}')
        return '\n'.join(lines)


config = Config()
