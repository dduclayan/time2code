"""TODO(dduclayan): DO NOT SUBMIT without one-line documentation for rm_small_files.

remove files less than 3Kb

TODO(dduclayan): DO NOT SUBMIT without a detailed description of rm_small_files.
"""

import os
import sys


def list_files_and_size(dir):
  for root, _, files in os.walk(dir):
    for file in sorted(files):
      file_size = os.path.getsize(root + file)

      print(f'{file} {file_size}KB')


def rm_small_files(dir):
  for root, _, files in os.walk(dir):
    for file in sorted(files):
      file_size = os.path.getsize(root + file)

      if file_size < 3000:
        print(f'removing {root + file}!')
        os.remove(root + file)


def main():
  small_file_dir = sys.argv[1]
  list_files_and_size(small_file_dir)
  print()
  rm_small_files(small_file_dir)

if __name__ == '__main__':
  main()
