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

if len(sys.argv) != 3:
    sys.exit('Usage: python downloader.py /path/to/mydesigns.csv /destination/path')

csv_path = sys.argv[1]
dest_path = sys.argv[2]

with open(csv_path, newline='', encoding='utf-8') as csv_file:
    row_count = sum(1 for row in csv.reader(csv_file)) - 1  # skip the header row
    print(f'{row_count} designs')

    csv_file.seek(0)
    count = 0

    reader = csv.DictReader(csv_file)
    for row in reader:
        count = count + 1
        filename = row['FILENAME']
        url = row['ART']

        print(f'Downloading {count}/{row_count} {filename}')

        path = dest_path + ('' if dest_path.endswith('/') else '/') + filename

        if not os.path.exists(path):
            download_path = path + '.downloading'
            urllib.request.urlretrieve(url, download_path)
            os.rename(download_path, path)
