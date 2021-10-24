import sys
import os
from time import time
from concurrent.futures import ThreadPoolExecutor
from sort import del_empty_folders
from pathlib import Path

def main (path):
    os.system (f"python sort.py {path}")


file_paths = sys.argv[1:]
x1 = time ()
with ThreadPoolExecutor(len (file_paths)) as executor:
    executor.map(main, file_paths)
# for path in file_paths:
#     main (path)
x2 = time ()
print (x2 - x1)

path = Path()
del_empty_folders(path)