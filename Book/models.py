from django.db import models

# Create your models here.

#  here App name is Book, model name is Book


class BookActiveManager(models.Manager):  # Custom Manager
    def get_queryset(self):
        return super(BookActiveManager, self).get_queryset().filter(is_deleted='N')   

class BookInactiveManager(models.Manager):  # Custom Manager
    def get_queryset(self):
        return super(BookInactiveManager, self).get_queryset().filter(is_deleted='Y')   



class Book(models.Model):
    # ID is by default created by Django in database table
    name = models.CharField(max_length=100)
    auther = models.CharField(max_length=100)
    qty = models.IntegerField()
    price = models.FloatField()
    is_published = models.BooleanField(default = False)
    is_deleted = models.CharField(max_length= 1, default= 'N')

    active_objects = BookActiveManager()
    inactive_objects = BookInactiveManager()
    objects = models.Manager()  

    def __str__(self):
        return f"{self.name} --------- {self.auther}"    # in admin window and in BOOK app records will show as f"{self.name} ---- {self.auther}"

    # to change table name useing class Meta
    class Meta:
        db_table = "bookinfo"    