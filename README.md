# OrbitKit Downloader

This is a simple python script that will download your OrbitKit design library. You will
need a recent version of Python and a CSV file that you have exported from OrbitKit.

1. Download `downloader.py` from https://github.com/orbitkit/downloader
2. Export your design metadata CSV from OrbitKit
3. Run the downloader:

Usage: `python downloader.py /path/to/mydesigns.csv /destination/path`

The script will download all designs listed in the CSV into the specified directory.
The directory must exist. If the script aborts, it can be restarted, and
it will pick up where it left off.

Caveat: It downloads your files with their original filenames. If multiple designs
have the same original filename, the second (and subsequent) designs will be ignored.