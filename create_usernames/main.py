"""TODO(dduclayan): DO NOT SUBMIT without one-line documentation for create_username.

output: a new file with username at the last column, the username is the first letter of the user and the lastname (e.g. Kasey Cook -> kcook). If there's collision for usernames, the new one should add the next available integer to its end (e.g. kcook, kcook2, kcook3) (we skip 1 to avoid confusion)

Firstname Lastname EmployeeID StartDate Username
Kasey Cook 1 10/13/2000 kcook
Kareem Dalby 4 10/16/2000 kdalby
Karter Cook 5 10/17/2000 kcook2
Kavan Cook 6 10/18/2000 kcook3

TODO(dduclayan): DO NOT SUBMIT without a detailed description of create_username.
"""
import sys


def create_username(file):
  usernames = {}
  output = []
  with open(file, 'r') as in_file:
    for line in in_file:
      words = line.split()
      username = words[0][0].lower() + words[1].lower()
      rest_of_line = ' '.join(words[:4])

      if username in usernames:
        usernames[username] += 1
        newusername = username + str(usernames[username])
        output.append(rest_of_line + ' ' + newusername)
      else:
        usernames[username] = 1
        output.append(rest_of_line + ' ' + username)

    with open('create_username_output.txt', 'w') as out_file:
      for line in output:
        out_file.write(line + ' \n')


def main():
  file = sys.argv[1]
  create_username(file)


if __name__ == '__main__':
  main()
