"""TODO(dduclayan): DO NOT SUBMIT without one-line documentation for find_disk_full_servers.

Plan:

1. Turn file into a list
2. Loop through lines
3. Split line
4. Delete words we don't need
5. Check if last element is > 85 (also need to account for 85.x)
6. Write element 1 and last element to file

TODO(dduclayan): DO NOT SUBMIT without a detailed description of find_disk_full_servers.
"""
import sys


def find_full_disk(file):
  disk_list = []
  full_disk_list = []

  with open(file, 'r') as in_file:
    for line in in_file:
      disk_list.append(line)

  for li in disk_list:
    words = li.split()
    del words[1:3]

    if float(words[-1].rstrip('%')) > 85:
      full_disk_list.append(words)

  with open('full_disk_output.txt', 'w') as out_file:
    for line in full_disk_list:
      out_file.write('%s\n' % line)


def main():
  file = sys.argv[1]
  find_full_disk(file)


if __name__ == '__main__':
  main()
