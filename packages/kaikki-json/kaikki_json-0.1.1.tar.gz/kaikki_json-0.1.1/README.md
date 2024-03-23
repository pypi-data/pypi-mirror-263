# kaikki_json

This is a package for downloading and reading data exported from [Wiktionary](https://www.wiktionary.org/) by [Kaikki.org](https://kaikki.org/).
There is a simple API that lets you iterate over the JSON objects, and process them however you like.

## Usage

### Install
```
pip install kaikki_json
```

### Quickstart

#### Download the data from Kaikki.org
```
python -m kaikki_json --download
```

#### Find and print the entry for the Spanish word 'hola'
```
>>> from kaikki_json import iter_items_in
>>> for item in iter_items_in('es'):
>>>    if item['word'] == 'hola':
>>>        print(item)
>>>        break
```

### Cache
kaikki_json caches the compressed data on disk.
It's decompressed automatically.
The total size used on the disk is about 2GB. 

#### Display cache location (and other info) 
```
python -m kaikki_json --info
```
