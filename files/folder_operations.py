import os

my_folder = os.path.join('..', 'data')

my_files = os.listdir(my_folder)
print(my_files)
fsize = os.path.getsize('../data/myfile.txt')
print(fsize)