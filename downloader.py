#!/usr/local/bin/python3
#
# Downloads art files for your OrbitKit design library.
#
# Usage: python downloader.py /path/to/mydesigns.csv /destination/path
#

import csv
import sys
import os
import urllib.request
import argparse


parser = argparse.ArgumentParser(
    usage="%(prog)s [OPTION] sourcecsv destdir",
    description="Download design image files from OrbitKit."
)
parser.add_argument("-u", "--unique", action='store_true', help='Make all filenames unique by prepending the design ID')
parser.add_argument('sourcecsv', help='Metadata CSV file you downloaded from OrbitKit')
parser.add_argument('destdir', help='Destination directory for image files')

args = parser.parse_args()

csv_path = args.sourcecsv
dest_path = args.destdir
unique = args.unique

with open(csv_path, newline='', encoding='utf-8') as csv_file:
    row_count = sum(1 for row in csv.reader(csv_file)) - 1  # skip the header row
    print(f'{row_count} designs')

    csv_file.seek(0)
    count = 0

    reader = csv.DictReader(csv_file)
    for row in reader:
        count = count + 1
        url = row['ART']
        filename = row['FILENAME']

        if unique:
            filename = row['ID'] + '-' + filename

        print(f'Downloading {count}/{row_count} {filename}')

        path = dest_path + ('' if dest_path.endswith('/') else '/') + filename

        if not os.path.exists(path):
            download_path = path + '.downloading'
            urllib.request.urlretrieve(url, download_path)
            os.rename(download_path, path)
