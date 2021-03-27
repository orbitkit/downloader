#!/usr/local/bin/python3
#
# Downloads art files for your OrbitKit design library.
#
# Usage: python downloader.py /path/to/mydesigns.csv /destination/path
#
# If you want OrbitKit to force the designs into the 4500x5400 merch format,
# pass the --merch and --secret flags. You will need to get the secret from
# your organization's settings page. Example
#
# python downloader.py --merch --secret 123456890 /path/to/mydesigns.csv /destination/path
#

import argparse
import csv
import os
import urllib.request


parser = argparse.ArgumentParser(
    usage="%(prog)s [OPTION] sourcecsv destdir",
    description="Download design image files from OrbitKit."
)
parser.add_argument("-u", "--unique", action='store_true', help='Make all filenames unique by prepending the design ID')
parser.add_argument("-m", "--merch", action='store_true', help='Intelligently convert images to merch format, 4500x5400')
parser.add_argument("-s", "--secret", help='Specify your organization secret key, required for --merch')
parser.add_argument('sourcecsv', help='Metadata CSV file you downloaded from OrbitKit')
parser.add_argument('destdir', help='Destination directory for image files')

args = parser.parse_args()

csv_path = args.sourcecsv
dest_path = args.destdir
unique = args.unique
merch = args.merch
secret = args.secret

if merch and not secret:
    raise Exception('When specifying --merch, you must also specify --secret')

with open(csv_path, newline='', encoding='utf-8') as csv_file:
    row_count = sum(1 for row in csv.reader(csv_file)) - 1  # skip the header row
    print(f'{row_count} designs')

    csv_file.seek(0)
    count = 0

    reader = csv.DictReader(csv_file)
    for row in reader:
        count = count + 1
        art = row['ART']
        filename = row['FILENAME']
        key = row['ID']

        if unique:
            filename = key + '-' + filename

        print(f'Downloading {count}/{row_count} {filename}')

        path = dest_path + ('' if dest_path.endswith('/') else '/') + filename

        if not os.path.exists(path):
            download_path = path + '.downloading'

            url = f'https://app.orbitkit.com/api/designs/{key}/render?X-Secret={secret}' if merch else art

            req = urllib.request.Request(url, data=None, headers={'User-Agent': "OrbitKit Downloader"})
            opened = urllib.request.urlopen(req)

            with open(download_path, 'wb') as f:
                f.write(opened.read())

            os.rename(download_path, path)
