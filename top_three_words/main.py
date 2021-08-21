"""TODO(dduclayan): DO NOT SUBMIT without one-line documentation for top_ten_words.

plan:
1. use dict. ex. word -> count
2. write dict.items() to list
3. sort list by count and return top ten

TODO(dduclayan): DO NOT SUBMIT without a detailed description of top_ten_words.
"""

import sys


def top_ten_words(file):
  filtered_words = ['if', 'the', 'and', 'i', 'is', 'an', 'has']
  puncuation = ['.', ',', '?', '!']
  word_count = {}
  word_count_list = []

  with open(file, 'r') as in_file:
    for line in in_file:
      words = line.split()
      for word in words:
        first_char = word[0]
        last_char = word[-1]

        if first_char in puncuation:
          stripped_word = word.lstrip(first_char)
          if stripped_word.lower() in filtered_words:
            pass
          elif stripped_word not in word_count:
            word_count[stripped_word] = 1
          else:
            word_count[stripped_word] += 1

        elif last_char in puncuation:
          stripped_word = word.rstrip(last_char)

          if stripped_word.lower() in filtered_words:
            pass
          elif stripped_word not in word_count:
            word_count[stripped_word] = 1
          else:
            word_count[stripped_word] += 1

        else:
          if word.lower() in filtered_words:
            pass
          elif word not in word_count:
            word_count[word] = 1
          else:
            word_count[word] += 1

  for word, count in word_count.items():
    word_count_list.append([word, count])

  top_ten = sorted(
      word_count_list, key=lambda x: x[1], reverse=True)[:11]

  for word, count in top_ten:
    print(f'{word} -> {count}')


def main():
  try:
    file = sys.argv[1]
    top_ten_words(file)
  except IndexError as e:
    raise e


if __name__ == '__main__':
  main()
