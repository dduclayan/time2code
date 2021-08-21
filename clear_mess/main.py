"""TODO(dduclayan): DO NOT SUBMIT without one-line documentation for clear_mess.

plan:
1. b/c we need to sort, we will add contacts to a list
2. we will find the user/date/ph thru regex search
3. after adding all contact info to list, run 'sorted()' on it
4. write the list to new file

TODO(dduclayan): DO NOT SUBMIT without a detailed description of clear_mess.
"""
import re
import sys


def clear_mess(file):
  users = []
  username_r = r'[a-zA-Z]+'
  date_r = r'(?:[0-9]{2}\/){2}[0-9]{4}'
  ph_r = r'(?:[0-9]{3}-){2}[0-9]{4}'

  with open(file, 'r') as in_file:
    for line in in_file:
      username = re.search(username_r, line)
      date = re.search(date_r, line)
      ph = re.search(ph_r, line)

      users.append((username.group(), ph.group(), date.group()))

  sorted_users = sorted(users, key=lambda x: x[0])

  with open('clear_mess_output.txt', 'w') as out_file:
    out_file.write('Username Phone_num Start_date\n')
    for user in sorted_users:
      out_file.write(' '.join(user) + '\n')


def main():
  file = sys.argv[1]
  clear_mess(file)


if __name__ == '__main__':
  main()
