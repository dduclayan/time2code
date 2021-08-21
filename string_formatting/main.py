"""TODO(dduclayan): DO NOT SUBMIT without one-line documentation for string_formatting.

plan:
1. create a for in range loop that loops until n
2. simple print of i in the various formats that the problem asks

sample outout:
16    20    10 10000
17    21    11 10001

TODO(dduclayan): DO NOT SUBMIT without a detailed description of string_formatting.
"""


def format_string(n):
  try:
    n = int(n)
  except ValueError:
    print("Input needs to be a number!")
  for i in range(1, n + 1):
    print(
        str(i) + ' ' + str(oct(i)[2:]) + ' ' + str(hex(i)[2:]) + ' ' +
        str(bin(i)[2:]))


def main():
  format_string(17)


if __name__ == '__main__':
  main()
