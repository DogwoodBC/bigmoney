"""
Takes BC Elections SA1 political contributions data in tab-separated format,
parses it and saves it into various data tables as appropriate.
"""

import os
import django
import argparse
import codecs
import csv

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'bigmoney.settings')
# sys.path.append('/data/web/placespeak.com/webapps/place')
django.setup()

from data.models import ElectoralDistrict


def main(args):
    print('Beginning import')

    file = codecs.open(args.input, 'r', args.encoding)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Takes BC Elections SA1 political contributions data in tab-separated '
                                                 'format, parses it and saves it into various data tables as appropriate.')

    parser.add_argument('-i', '--input', required=False, action='store', help='Path to the input file.')
    parser.add_argument('-e', '--encoding', action='store', default='iso8859_2', help='Encoding of the input file. Defaults to iso8859_2, aka Latin-2.')

    args = parser.parse_args()
    main(args)
