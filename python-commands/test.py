
# nums = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']

# al = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']

# my_dict = {n1: al1 for n1, al1 in zip(nums, al)}

# print my_dict


# import os
# from datetime import datetime
# print(dir(os))

# print(os.getcwd())

# os.chdir('/home/jacksparrow/Desktop/python-scripts/python-commands')                # change in directory.
# print(os.getcwd())

# print(os.stat('sorting.txt').st_mtime)

# mod = os.stat('sorting.txt').st_mtime
# print(datetime.fromtimestamp(mod))

# for dirpath, dirnames, filenames in os.walk('/home/jacksparrow/Desktop/python-scripts'):

#     print("current path:",dirpath)
#     print("directories name:",dirnames)
#     print("filenames:",filenames)


# with open('List', 'r') as f:
#     pass
# print(f.closed)

# with open('List', 'r') as f:
#     f_contents = f.read()
#     print(f_contents)

# with open('List', 'r') as f:
#     f_contents = f.readline()
#     print(f_contents)

#     f_contents = f.readline()
#     print(f_contents)

#     f_contents = f.readline()
#     print(f_contents)

#     f_contents = f.readline()
#     print(f_contents)

#     f_contents = f.readline()
#     print(f_contents, end=' ')

#     for line in f:
#         print(line,end=' ')


# with open('test2.txt', 'w') as f:
#     f.write('hi iam shravan')
#     f.seek(0)
#     f.write('k')

# copies one from another.
# sum = 0
# with open('List', 'r') as rf:
#     with open('List_copy', 'w') as wf:
#         for line in rf:
#             wf.write(line)
#             sum = sum + 1
#             print(sum)

# writes image files
# with open('ubu.jpg', 'rb') as rf:
#     with open('ubu_copy.jpg', 'wb') as wf:
#         chunk_size = 4096
#         rf_chunk = rf.read(chunk_size)
#         while len(rf_chunk) > 0:
#             wf.write(rf_chunk)
#             rf_chunk = rf.read(chunk_size)
# my_nums = (x * x for x in [1, 2, 3, 4, 5])
# # here if we use square brackets we get list, for using () we are getting generators

# print (my_nums)  # [1, 4, 9, 16, 25]
# print next(my_nums)
# print next(my_nums)
# print next(my_nums)
# print next(my_nums)
# print next(my_nums)

import random


def numsint():
    sum = random.randint(0, 100) + random.randint(0, 10000)
    return sum


f = numsint
print(f())
