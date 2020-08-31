from django.db import models

class Item (models.Model):
    text = models.TextField(default='')

class Pd (models.Model):
    name = models.TextField(default='')
    email = models.TextField(default='')
    phone_number = models.TextField(default='')
    adress = models.TextField(default='')

class Pp (models.Model):
    description = models.TextField(default='')

class E (models.Model):
    school = models.TextField(default='')
    subject = models.TextField(default='')
    start = models.DateField(default='')
    end = models.DateField(default='')

class WE (models.Model):
    company = models.TextField(default='')
    job = models.TextField(default='')
    description = models.TextField(default='')
class I (models.Model):
    interest= models.TextField(default='')

class R (models.Model):
    name= models.TextField(default='')
    phone = models.TextField(default='')
    email = models.TextField(default='')
# Create your models here.
 