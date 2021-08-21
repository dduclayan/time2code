"""TODO(dduclayan): DO NOT SUBMIT without one-line documentation for sort_assets.

plan:
1. creat function that sorts assets
2. create function that prepends the asset# s

TODO(dduclayan): DO NOT SUBMIT without a detailed description of sort_assets.
"""

from datetime import datetime
import sys


def sort_assets(file):
  with open(file, 'r') as in_file, open('new_assets.txt', 'w') as out_file:
    assets_list = []
    first_line = 'Asset# ' + in_file.readline()  # skips header
    for line in in_file:
      assets_list.append(line.split())

    sorted_assets_list = sorted(
        assets_list, key=lambda x: (x[0], datetime.strptime(x[1], '%m/%d/%Y')))
    asset_num = 0

    out_file.write(first_line)
    for line in sorted_assets_list:
      line = ' '.join(line)
      asset_num += 1
      out_file.write(str(asset_num).zfill(6) + ' ' + line + '\n')


def main():
  file = sys.argv[1]
  sort_assets(file)


if __name__ == '__main__':
  main()
