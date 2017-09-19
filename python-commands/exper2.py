# # import os

# # # for dirpath, dirnames, filenames in os.walk('/home/jacksparrow/Desktop/python-scripts'):

# # #     print("current path:",dirpath)
# # #     print("directories name:",dirnames)
# # #     print("filenames:",filenames)


# # print(os.environ.get('HOME'))

# '/home/jacksparrow/Desktop/python-scripts/python-commands/SampleCSVFile_119kb.csv'

# import csv

# with open('SampleCSVFile_119kb.csv', 'r') as csv_file:
#     csv_reader = csv.reader(csv_file)

#     # next(csv_reader)

#     with open('newCsv_file.csv', 'w') as new_file:
#         csv_writer = csv.writer(new_file, delimiter='\t')
#         for line in csv_reader:
#             csv_writer.writerow(line)


# print('finish')


# class Employee:

#     def __init__(self, first, last, pay):
#         self.first = first
#         self.last = last
#         self.email = first + '.' + last + '@email.com'
#         self.pay = pay

#     def fullname(self):
#         return '{} {}'.format(self.first, self.last)


# emp_1 = Employee('Corey', 'Schafer', 50000)
# emp_2 = Employee('Test', 'Employee', 60000)

# print(emp_1)
# print(emp_2)


# print(emp_1.email)

# print(emp_2.email)
# print(emp_1.fullname())
# print(emp_2.fullname())


# class Employee:

#     raise_amount = 1.5                                                        # this is class variable.

#     def __init__(self, first, last, pay):
#         self.first = first
#         self.last = last
#         self.email = first + '.' + last + '@email.com'
#         self.pay = pay

#     def fullname(self):
#         return '{} {}'.format(self.first, self.last)


# emp_1 = Employee('Corey', 'Schafer', 50000)
# emp_2 = Employee('Test', 'Employee', 60000)

# print(emp_1.__dict__)
# print(emp_2.__dict__)
# print(Employee.__dict__)

# emp_1.raise_amount = 2.0

# print(Employee.raise_amount)
# print(emp_1.raise_amount)
# print(emp_2.raise_amount)

