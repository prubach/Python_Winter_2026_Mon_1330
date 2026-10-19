import os

#my_file = 'data/myfile.txt'
my_file = os.path.join('../data', 'myfile.txt')
my_file = '../data/myfile.txt'

#my_file = 'C:/Users/prubac/PycharmProjects/Python_Winter_2026_Mon_1330/data/myfile.txt'
# Current working directory
cwd = os.getcwd()
print(cwd)


f = open(my_file)
lines = f.readlines()
for line in lines:
    print(line, end='')
f.close()

print('\n' + '-'*80)



with open(my_file, 'r') as f:
    lines = f.readlines()
    for line in lines:
        print(line, end='')

