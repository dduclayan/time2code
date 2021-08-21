"""TODO(dduclayan): DO NOT SUBMIT without one-line documentation for strong_pw.

plan:
1. create var(int) called "score"
2. +1 to score if pw has a number, or lower_case, upper_case, special_char
3. use any() to test if iterable matches n, l, u, s
4. return either score or 6-n


pw req:
len = 6
contain 1 digit
one lowercase eng char
one uppercase eng char
one special char


TODO(dduclayan): DO NOT SUBMIT without a detailed description of strong_pw.
"""


def minimum_num(n, password):
  special_characters = "!@#$%^&*()-+"

  score = 0

  if not any(x.islower() for x in password):
    score += 1
  if not any(x.isdigit() for x in password):
    score += 1
  if not any(x.isupper() for x in password):
    score += 1
  if not any(x for x in special_characters):
    score += 1

  y = max(score, 6-n)
  print(y)
  return y


def main():
  minimum_num(3, "Ab1")
  minimum_num(11, "#HackerRank")
  minimum_num(2, "d@")


if __name__ == "__main__":
  main()
