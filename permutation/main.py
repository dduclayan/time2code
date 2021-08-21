"""TODO(dduclayan): DO NOT SUBMIT without one-line documentation for permutation.

1. run sorted() on strings and check if x == y

TODO(dduclayan): DO NOT SUBMIT without a detailed description of permutation.
"""

def is_permutation(str1, str2):
  x = sorted(str1)
  y = sorted(str2)
  print(x, y)
  return sorted(str1) == sorted(str2)


def main():
  print(is_permutation('dog', 'ogD'))


if __name__ == '__main__':
  main()
