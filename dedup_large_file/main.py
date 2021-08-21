"""TODO(dduclayan): DO NOT SUBMIT without one-line documentation for dedup_file.

plan:
1. add lines to a list
2. loop through list and add them to a dict to remove dupes
3. write key(line) to file

can't use set. sets are unordered and you can't run sorted() on them.
could use ordered dict

TODO(dduclayan): DO NOT SUBMIT without a detailed description of dedup_file.
"""

import sys


def dedup(file):
  """Turns the lines of a file into a dict, then write dict to file."""
  file_lines = []
  file_dict = {}

  with open(file, 'r') as in_file:
    file = [line.rstrip() for line in in_file]
    for li in file:  # O(n)
      file_lines.append(li)

  for line in file_lines:  # O(n)
    file_dict[line] = 1

  with open('new_file1.txt', 'w') as out_file:
    for key in file_dict:  # O(n)
      out_file.write(key + '\n')


def main():
  file = sys.argv[1]
  dedup(file)


if __name__ == '__main__':
  main()
