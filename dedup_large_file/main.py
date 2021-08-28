"""TODO(dduclayan): DO NOT SUBMIT without one-line documentation for dedup_large_file.

There are so many duplicated lines and you will need to remove them and return a
new file that only contains unique lines.
Assume all unique lines will fit in memory.

plan:
1. make a generator function to yield lines of the file
2. add lines to set()
-- set() only has unique values

questions:
1. Do lines need to be ordered or sorted?
-- if not, can use set()
-- if so, need to use list and a dict to remove dupes


TODO(dduclayan): DO NOT SUBMIT without a detailed description of dedup_large_file.
"""

import sys


def generator(file):
  with open(file) as in_file:
    for line in in_file:
      yield line


def dedup_large_file():
  file = sys.argv[1]
  lines = set()

  for line in generator(file):
    lines.add(line)

  with open('dedup_out.txt', 'w') as out_file:
    out_file.writelines(lines)

    
def main():
  dedup_large_file()


if __name__ == '__main__':
  main()
