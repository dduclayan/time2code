"""TODO(dduclayan): DO NOT SUBMIT without one-line documentation for sort_file_by_date.

plan:
1. split line
2. convert datetime to datetime object
3. add filename, datetime, datetime obj to list
4. sort by datetime obj


TODO(dduclayan): DO NOT SUBMIT without a detailed description of sort_file_by_date.
"""

from datetime import datetime
import sys


def sort_file_by_date(file):
  li = []
  with open(file, 'r') as in_file:
    for line in in_file:
      words = line.split()
      date_string = ' '.join(words[2:5])
      file_name = words[-1]
      date_obj = datetime.strptime(date_string, '%B %d, %Y')
      li.append((date_string, date_obj, file_name))
  sorted_dates = li.sort(li, key=lambda x: (x[1]), reverse=True)
  for k, v, i in sorted_dates:
    print(k, ',', i)


def main():
  file = sys.argv[1]
  sort_file_by_date(file)


if __name__ == '__main__':
  main()
