"""TODO(dduclayan): DO NOT SUBMIT without one-line documentation for file_manipulation.

plan:
1. look for files ending in .jpg -> file.endswith('.jpg') then move to new dir
2. look for files ending in .jpg -> file.endswith('.html') then move to new dir
3. write all .txt files to a list then write list to file


TODO(dduclayan): DO NOT SUBMIT without a detailed description of file_manipulation.
"""

import os
import shutil


def file_manipulation(directory):
  # create dir to hold .jpgs
  picture_dir_path = '/google/src/cloud/dduclayan/daily-coding-challenge/google3/experimental/users/dduclayan/python/file_manipulation_dir/pictures/'
  if os.path.exists(picture_dir_path):
    shutil.rmtree(picture_dir_path)
  os.mkdir(picture_dir_path)

  parent_path = '/google/src/cloud/dduclayan/daily-coding-challenge/google3/experimental/users/dduclayan/python/file_manipulation_dir/'
  for file in os.listdir(directory):
    txt_files = []
    # changes file into /path/to/file
    # file_path = os.fsdecode(file)
    if file.endswith('.html'):
      pre, _ = os.path.splitext(file)
      os.rename(parent_path + file, parent_path + pre + '.htm')
      # print(f'pre = {pre}')
    if file.endswith('.jpg'):
      os.path.join(picture_dir_path, file)
    if file.endswith('.txt'):
      txt_files.append(file)

    txt_files.sort()
    with open('stuff.txt', 'w'):
      for file in txt_files:
        



def main():
  directory = '/google/src/cloud/dduclayan/daily-coding-challenge/google3/experimental/users/dduclayan/python/file_manipulation_dir'
  file_manipulation(directory)


if __name__ == '__main__':
  main()
