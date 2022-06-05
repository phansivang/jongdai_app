from django.db import models
from django.contrib.auth.admin import User
import time

COLOR_CHOICES = (
    ('FEMALE','FEMALE'),
    ('MALE','MALE')
)
named_tuple = time.localtime() # get struct_time
time_string = time.strftime("%d:%m/%H:%M %p", named_tuple)

class cash_male(models.Model):
    dollar = models.IntegerField(blank=True)
    riel = models.IntegerField(blank=True)
    guest_name = models.CharField(max_length=26,blank=True)
    sex = models.CharField(max_length=20,blank=True)
    datetime = models.DateTimeField(auto_now=True,blank=True)
    date = models.CharField(max_length=20,default=time_string,blank=True)
    author = models.ForeignKey(User,on_delete=models.CASCADE, blank=True)

    class Meta:
        ordering = ['-datetime']
    def __str__(self):
        return self.guest_name

class cash_female(models.Model):
    dollar = models.IntegerField(default='0',blank=True)
    riel = models.IntegerField(default='0',blank=True)
    guest_name = models.CharField(max_length=26,blank=True)
    sex = models.CharField(max_length=20,choices=COLOR_CHOICES,blank=True)
    datetime = models.DateTimeField(auto_now=True,blank=True)
    date = models.CharField(max_length=20,default=time_string,blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, blank=True,)

    class Meta:
        ordering = ['-datetime']

    def __str__(self):
        return self.guest_name

