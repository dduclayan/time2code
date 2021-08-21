"""TODO(dduclayan): DO NOT SUBMIT without one-line documentation for most_visited_websites.

plan:

1. split() the line so we can over each website 1 by 1
2. add the websites to dict and increment by 1
3. sorted() the dict
4. output first 5 key/values to file

TODO(dduclayan): DO NOT SUBMIT without a detailed description of most_visited_websites.
"""
import sys


def most_visited_websites(file):
  file_lines = []
  website_count = {}
  top_five_website_list = []

  with open(file, 'r') as in_file:
    for line in in_file:
      file_lines.append(line)

  for word in file_lines:
    words = word.split()
    for wo in words[1:]:  # O(n^2)
      if wo in website_count:
        website_count[wo] += 1
      else:
        website_count[wo] = 1

  sorted_websites = sorted(
      website_count.items(), key=lambda kv: (kv[1], kv[0]), reverse=True)[:5]

  print('sorted_websites: ', sorted_websites)

  for x, y in sorted_websites:
    print(f'{x} {y}')


def main():
  file = sys.argv[1]
  most_visited_websites(file)


if __name__ == '__main__':
  main()
