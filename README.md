# OrbitKit Downloader

This is a simple python script that will download your OrbitKit design library. You will
need a recent version of Python and a CSV file that you have exported from OrbitKit.

Usage: `python downloader.py /path/to/mydesigns.csv /destination/path`

The script will download all designs listed in the CSV into the specified directory.
The directory must exist.

If the script is aborted or errors out, it can be restarted. It will pick up where it left off.