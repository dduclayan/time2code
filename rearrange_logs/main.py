"""TODO(dduclayan): DO NOT SUBMIT without one-line documentation for reasonable_costs.

output:
the lines sorted by date where cost is between $20 and $50, and recommended is Yes

plan:
1. read file line by line, check if recommended is yes -> add to list
2. read through list, split line, check if price is between 20 and 50 -> add to new list
3. read thru list, split line, lambda sort date

time complexity:
O(n log n) due to sorted()?
"""
import sys
from datetime import datetime


def reasonable_costs(file):
  is_recommended = []
  is_between_20_and_50 = []
  with open(file, 'r') as in_file:
    first_line = in_file.readline()  # skip first line which is just headers
    for line in in_file:
      segment = line.split()
      if segment[3] == 'Yes':
        is_recommended.append(line.rstrip('\n'))

  for item in is_recommended:
    segment = item.split()
    date_str = segment[0]
    city = segment[1]
    recommended_status = segment[-1]
    date_obj = datetime.strptime(date_str, '%m/%d/%y')  # need to convert to a datetime obj to be able to compare/sort
    cost = float(segment[2].lstrip('$'))
    if cost > 20 and cost < 50:
      is_between_20_and_50.append((date_obj, city, cost, recommended_status))

  sorted_by_date = sorted(is_between_20_and_50, key=lambda x: (x[0]))
  for k, v, i, x, in sorted_by_date:
    print(k.strftime('%m/%d/%y'), v, i, x)


def main():
  file = sys.argv[1]
  reasonable_costs(file)


if __name__ == '__main__':
  main()
