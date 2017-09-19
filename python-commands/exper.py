
li = [9, 4, 5, 2, 5, 7, 8, 1, 6, 3]

sorted_li = sorted(li, reverse=True)
print("sorted list is :\t", sorted_li)

li.sort(reverse=True)                                                           # here list is sorted in reverse order.
print('Original Variables:\t', li)


tup = (9, 4, 5, 2, 5, 7, 8, 1, 6, 3)
sort_tup = sorted(tup)
print(sort_tup)  # tuples do not have sort method


student = {'name': 'John', 'age': 25, 'courses': 'Math'}

sort_student = sorted(student)
print(sort_student)


li = [-9, 4, -5, -2, 5, -7, 8, 1, 6, 3]
s_li = sorted(li, key=abs)                                              # key parameter absolute is used here to sort things out.
print(s_li)  # [1, -2, 3, 4, -5, 5, 6, -7, 8, -9]. here in key parameter you can also pass return value of a fuction.


import datetime

my_date = datetime.datetime(2016, 9, 24, 12, 30, 45)

print(my_date)

sentence = '{:%B %d, %Y}'.format(my_date)
print(sentence)

sentence = '{0:%B %d, %Y} fell on a {0:%A} and was the {0:%j} day of the year'.format(my_date)
print(sentence)
