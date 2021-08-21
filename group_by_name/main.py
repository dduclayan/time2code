"""
plan:
1. add line to a list
2. run sort on list and lambda sort and group by the groupname

sort() - use on an existing list, returns None
sorted() - can be used on any iterable, returns a new list
"""

import sys


def GroupByGroupName(file):
  """Takes in a file and groups lines by groupname."""
  with open(file, 'r') as in_file:
    groups = []

    for line in in_file:
      groups.append(line)
    # sorts by the second field in the line
    groups.sort(key=lambda word: word.split(' ')[1].lower())

    with open('new_file', 'w') as out_file:
      s = ListToString(groups)
      out_file.write(s)


def ListToString(s):
  string = ''
  return string.join(s)


def main():
  file = sys.argv[1]
  GroupByGroupName(file)


if __name__ == '__main__':
  main()
