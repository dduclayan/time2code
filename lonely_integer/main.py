"""TODO(dduclayan): DO NOT SUBMIT without one-line documentation for lonely_int.

plan:
1. go through list and add them to a dict
2. if key is in dict, +1 to value. if not, key[value] = 1
3. loop through dict and print out the key that has a value of 1


TODO(dduclayan): DO NOT SUBMIT without a detailed description of lonely_int.
"""


def lonely_int(nums):
  d = {}
  for num in nums:
    if num in d:
      d[num] += 1
    if num not in d:
      d[num] = 1

  for k, v in d.items():
    if v == 1:
      return k


def main():
  a = [1, 2, 3, 4, 3, 2, 1]
  lonely_int(a)

if __name__ == '__main__':
  main()

