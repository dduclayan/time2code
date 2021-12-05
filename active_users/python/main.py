"""TODO(dduclayan): DO NOT SUBMIT without one-line documentation for active_users.

You are working in yaboo and need to find out the active users and their phone
numbers.

If active users not not found in FileA, you use your
company main line number (444) 123-1233

input: FileA, FileB
output: active users and their phone numbers in format
username (xxx) xxx-xxxx

plan:
1. find active users in 'is_active_file' and put them in a list
2. read through 'username_contact_file' line by line, split the email by '@'
and see if there is a match in the 'is_active_list'
3. if there is a match, print out the username and ph.
4. if no match, print out the username and company ph.


TODO(dduclayan): DO NOT SUBMIT without a detailed description of active_users.
"""
import sys


def active_users(username_contact_file, is_active_file):
  is_active = set()
  with open(username_contact_file, 'r') as in_file_1, open(is_active_file,
                                                           'r') as in_file_2:
    for line in in_file_2:
      segment = line.split()
      if segment[1] == 'Yes':
        is_active.add(segment[0])

    for line in in_file_1:
      segment = line.split('@')
      username = segment[0]
      after_at_segment = segment[1].split()
      phone = ' '.join(after_at_segment[1:3])

      if username in is_active:
        print(f'{username} {phone}')
        is_active.remove(username)

    for remaining_users in is_active:
      print(f'{remaining_users} (444) 123-1233')


def main():
  file = sys.argv[1]
  file2 = sys.argv[2]
  active_users(file, file2)

if __name__ == '__main__':
  main()
