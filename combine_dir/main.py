"""

plan:
1. os.walk() through dir 1, create a dict of dir1's files as [filename: subdir/filename]
2. os.walk() through dir 2, check if file is in the dict, if it is, append '_2'
3. create 'new_dir', create files from dict into 'new_dir'

"""

import os
import shutil


def combine_two_dir(dir1, dir2):
  dir_dict = {}
  new_dir = '/google/src/cloud/dduclayan/daily-coding-challenge/google3/experimental/users/dduclayan/python/new_dir'

  for root, _, files in os.walk(dir1):
    subdir = root.split('/')[-1]
    for file in files:
      subdir_file = subdir + '/' + file
      dir_dict[file] = subdir_file

  for root, _, files in os.walk(dir2):
    subdir = root.split('/')[-1]
    for file in files:
      subdir_file = subdir + '/' + file
      if file in dir_dict:
        dir_dict[file] = subdir_file + '_2'

  os.makedirs('new_dir', exist_ok=True)

  for _, subdir_file in dir_dict.items():
    subdir = subdir_file.split('/')[0]
    filename = subdir_file.split('/')[1]

    if subdir == 'dir2':
      path = os.path.join(new_dir, filename)
      open(path, 'w')

    if subdir[:7] == 'sub_dir':
      dir_path = os.path.join(new_dir, subdir)
      file_path = os.path.join(dir_path, filename)
      os.makedirs(dir_path)
      open(file_path, 'w')


def main():
  dir1 = '/google/src/cloud/dduclayan/daily-coding-challenge/google3/experimental/users/dduclayan/python/dir1'
  dir2 = '/google/src/cloud/dduclayan/daily-coding-challenge/google3/experimental/users/dduclayan/python/dir2'

  combine_two_dir(dir1, dir2)

  # shutil.rmtree(dir1, ignore_errors=True)
  # shutil.rmtree(dir2, ignore_errors=True)

if __name__ == '__main__':
  main()


