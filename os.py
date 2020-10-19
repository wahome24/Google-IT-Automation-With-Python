#This simple code showcase how to check for files or directory using the OS python module

import os

#create a variable and assign it the name of the directory containing your files and other directories.
dir = 'Derano'

for name in os.listdir(dir): #lists the content of the directory
  #creats a path in the format dir/name of file or directory
  fullname = os.path.join(dir,name)

 # check for either file or directory
  if os.path.isdir(fullname):
    print(f'{fullname} is a directory!')
  else:
    print(f'{fullname} is a file!')
