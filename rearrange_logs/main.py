"""TODO(dduclayan): DO NOT SUBMIT without one-line documentation for rearrange_logs.

question:
can I assume that the log file is already sorted by date?

plan:
1. create dict for each api call to count calls
2. read through log files line by line
3. if line contains '<api call>', add line to '<api> file'


TODO(dduclayan): DO NOT SUBMIT without a detailed description of rearrange_logs.
"""
import sys


def rearrange_logs(files):
  log_files = []

  for file in files:
    log_files.append(file)

  get_dict = {}
  add_dict = {}
  set_dict = {}
  with open('get_log.txt',
            'w') as get_log_out, open('set_log.txt', 'w') as set_log_out, open(
                'add_log.txt', 'w') as add_log_out:
    for file in log_files:
      with open(file, 'r') as in_file:
        for line in in_file:
          segment = line.split()
          date = segment[1]
          call = segment[2]

          if call == 'Get':
            get_log_out.write(line)
            if date in get_dict:
              get_dict[date] += 1
            else:
              get_dict[date] = 1

          if call == 'Set':
            set_log_out.write(line)
            if date in set_dict:
              set_dict[date] += 1
            else:
              set_dict[date] = 1

          if call == 'Add':
            add_log_out.write(line)
            if date in add_dict:
              add_dict[date] += 1
            else:
              add_dict[date] = 1

  with open('stats_log.txt', 'w') as stats_log_out:
    stats_log_out.write('Get\n')
    for k, v in get_dict.items():
      stats_log_out.write(k + ' ' + str(v) + '\n')
    stats_log_out.write('Set\n')
    for k, v in set_dict.items():
      stats_log_out.write(k + ' ' + str(v) + '\n')
    stats_log_out.write('Add\n')
    for k, v in add_dict.items():
      stats_log_out.write(k + ' ' + str(v) + '\n')


def main():
  files = sys.argv[1:]
  rearrange_logs(files)


if __name__ == '__main__':
  main()
