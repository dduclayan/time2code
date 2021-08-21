"""TODO(dduclayan): DO NOT SUBMIT without one-line documentation for qps_per_server.

plan:
1. store in dict - [(server_id, time)]: count
ex.
[(server1, 5:05:03)]: 2, [(server2, 5:05:03)]: 2

for server, time, count in dict.items():
  print(f'{server}  {QPS}')

Clarifying questions:
1. Do we want to return an int or float?
2. Are query_IDs unique?


TODO(dduclayan): DO NOT SUBMIT without a detailed description of qps_per_server.
"""
import sys


def find_qps(file):
  with open(file, 'r') as in_file:
    first_line = in_file.readline()
    server_count = {}
    server1_count = 0
    server2_count = 0
    server3_count = 0
    amt_of_secs = set()

    for line in in_file:
      segment = line.split()
      time = segment[0]
      server = segment[2]

      if time not in amt_of_secs:
        amt_of_secs.add(time)

      if (server, time) in server_count:
        server_count[(server, time)] += 1
      else:
        server_count[(server, time)] = 1

    for (server, time), count in server_count.items():
      if 'server1' in (server, time):
        server1_count += count
      if 'server2' in (server, time):
        server2_count += count
      if 'server3' in (server, time):
        server3_count += count

    print('Server_ID QPS')
    print(f'Server1 {round(server1_count/len(amt_of_secs))}')
    print(f'Server2 {round(server2_count/len(amt_of_secs))}')
    print(f'Server3 {round(server3_count/len(amt_of_secs))}')


def main():
  file = sys.argv[1]
  find_qps(file)


if __name__ == '__main__':
  main()
