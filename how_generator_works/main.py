"""TODO(dduclayan): DO NOT SUBMIT without one-line documentation for generator.

1. use generator to return value
2. add value to a list
3. return sum / len(list)

TODO(dduclayan): DO NOT SUBMIT without a detailed description of generator.
"""
import sys


def generator(file):
  with open(file, 'r') as in_file:
    for line in in_file:
      yield int(line)


def find_avg():
  file = sys.argv[1]
  total = 0
  num_len = 0

  for num in generator(file):
    total += num
    num_len += 1

  return int(sum / num_len)


def main():
  print(find_avg())


if __name__ == '__main__':
  main()
