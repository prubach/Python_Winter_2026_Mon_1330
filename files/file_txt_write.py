import os
my_file = os.path.join('..', 'data', 'myfile_out.txt')

f = open(my_file, 'w')
f.write('Hello World\n')
f.write('Python here\n')
f.flush()
f.write('At SGH\n')
f.close()

with open(my_file, 'a') as f:
    f.write('Appending this\n')