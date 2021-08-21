"""

plan:
1. add pid: start time, end time to d
2. calculate time spent and add it to list
3. sort list by pid

"""

import sys
from datetime import datetime


def clear_things_up(file):
  d = {}
  with open(file, 'r') as in_file:
    first_line = in_file.readline()
    for line in in_file:
      words = line.split()
      pid = words[2]
      time = words[0]
      day = words[1]

      if pid not in d:
        d[pid] = []
      if pid in d:
        d[pid] += [time + ' ' + day]

  for pid, times in sorted(d.items(), key=lambda i: i[0]):
    print(pid + ' ' + calc_time(times[0], times[1]))


def calc_time(start, end):
  a = datetime.strptime(end, '%H:%M:%S %m/%d/%Y')
  b = datetime.strptime(start, '%H:%M:%S %m/%d/%Y')
  c = a - b
  return str(c)


def main():
  file = sys.argv[1]
  clear_things_up(file)


if __name__ == '__main__':
  main()
