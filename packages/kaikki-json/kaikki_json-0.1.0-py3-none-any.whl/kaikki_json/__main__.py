
import argparse

from kaikki_json._private.config import config
from kaikki_json._private.download import download_kaikki

parser = argparse.ArgumentParser(
    prog='Kaikki JSON',
    description='Download and read Wiktionary data in JSON format, using Kaikki data dumps.',
)

group = parser.add_mutually_exclusive_group(required=True)
group.add_argument('-d', '--download', action='store_true', help='download Wiktionary data from Kaikki')
group.add_argument('-i', '--info', action='store_true', help='display useful info')

parser.add_argument('-q', '--quiet', action='store_true', help='hide console output')
parser.add_argument('-f', '--force', action='store_true', help='force download, even if file is already present')

args = parser.parse_args()

if args.download:
    download_kaikki(args.force, not args.quiet)

if args.info:
    print(config)
