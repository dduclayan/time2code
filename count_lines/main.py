"""TODO(dduclayan): DO NOT SUBMIT without one-line documentation for count_c.

plan:
1. count code block
- if first two char == '/*', set 'is_code_block' to True
- if 'is_code_block' == True, comments += 1

2. count regular comments
- if line[1:] == '//', comments += 1

3. print(code_lines - comments)

TODO(dduclayan): DO NOT SUBMIT without a detailed description of count_c.
"""
#!/usr/bin/python
import sys


def count_lines_of_code(file):
  with open(file, 'r') as in_file:
    comments = 0
    code_lines = 0
    is_code_block = False

    for line in in_file:
      code_lines += 1
      # count code block comments
      if line[:2] == '/*':
        is_code_block = True
        comments += 1
      elif is_code_block:
        comments += 1
      elif line[-2:] == '*/':
        is_code_block == False
        comments += 1

      # count regular comments
      if line[:2] == '//' and not is_code_block:
        comments += 1

    print(f'{code_lines} - {comments}')


def main():
  file = sys.argv[1]
  count_lines_of_code(file)

if __name__ == '__main__':
  main()

