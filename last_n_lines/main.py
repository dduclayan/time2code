"""TODO(dduclayan): DO NOT SUBMIT without one-line documentation for last_n_lines.

plan:
1. open file
2. write all lines to a list
3. return/print last n lines
-- ex
-- print list[-n:]

edge cases:
1. what if 'n' is a negative number?

TODO(dduclayan): DO NOT SUBMIT without a detailed description of last_n_lines.
"""
import sys


def last_n_lines(file, n):
  # I believe this method should be better than read() since read() will fail
  # if the file is too large.
  file_lines = []
  with open(file, 'r') as in_file:
    for line in in_file:
      file_lines.append(line)

  for line in file_lines[-n:]:
    print(line.strip('\n'))


def main():
  file = sys.argv[1]
  last_n_lines(file, 3)


if __name__ == '__main__':
  main()
