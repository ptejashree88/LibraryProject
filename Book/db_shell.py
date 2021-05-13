from Book.models import Book

import random

# CRUD operations

# create book (enter book entry in database)
'''
b = Book.objects.create(name = "Python", auther = "Abc", qty = 45, price = 550)

def Create_name():
    name = ""
    for i in range(random.randint(4,7)):
        name += chr(random.randint(65,90))
    # print(name)
    return name

for book in range(1, 10):
    b = Book(name = Create_name(), auther = Create_name(), qty = (random.randint(20, 50)), price = (random.randint(200, 850)))
    Book.save(b)
'''

# Read all data from database
'''
# data = Book.objects.all()
# print(data)

# print(Book.objects.all())
# print(Book.objects.all().values())
# print(Book.objects.all().count())

# print(Book.objects.values('id', 'name', 'auther'))

all_data = Book.objects.all()
# for book in all_data:
#     print(book)

for Book in all_data:
    print(Book.__dict__)
    
# when
# all_data_1 = Book.objects.all().values()
# for Book in all_data:
#     print(Book)
'''

# Read single value from database

# b1 = Book.objects.get(id = 25)
# print(b1)


# update data
'''
up_b = Book.objects.get(id = 48)
up_b.name = "AAAAA"
up_b.auther = "Auther"
up_b.save()
'''

# delete data
'''
# del_b = Book.objects.get(id = 50)
# del_b.delete()

del_b1 = Book.objects.get(id = 49)
Book.delete(del_b1)
'''

# filter command

# fb = Book.objects.filter(id__gt = 5)            # __gt is for greater than, __gte for greater than equal to
# print(fb)

fb1 = Book.objects.filter(id__lt = 3)               # __lt is for less than, __lte for less than equal to
print(fb1)

fb2 = list(Book.objects.filter(id__in = [5, 6, 7]))
print(fb2)

fb3 = Book.objects.filter(id__in = [2, 3, 4, 5]).update(qty = 15)