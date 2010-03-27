from django.db import models
from django.contrib.localflavor.in_.forms import *


class group(models.Model):
    name = models.CharField(max_length=30)
    desc = models.CharField(max_length=300)

    def __unicode__(self):
        return self.name

class person(models.Model):
    name = models.CharField(max_length=30)
    group = models.ManyToManyField(group)
    address = models.CharField(max_length=300)
    city = models.CharField(max_length=30)
    state = INStateSelect
    phone1_type = models.CharField(max_length=30)
    phone1 = models.IntegerField()
    phone2_type = models.CharField(max_length=30)
    phone2 = models.IntegerField()
    phone3_type = models.CharField(max_length=30)
    phone3 = models.IntegerField()
    phone4_type = models.CharField(max_length=30)
    phone4 = models.IntegerField()
    phone5_type = models.CharField(max_length=30)
    phone5 = models.IntegerField()
    phone6_type = models.CharField(max_length=30)
    phone6 = models.IntegerField()
    email1 = models.EmailField(max_length=75)
    email2 = models.EmailField(max_length=75)
    website1 = models.URLField(max_length=75)
    email1 = models.EmailField(max_length=75)
    email2 = models.EmailField(max_length=75)
    website1 = models.URLField(max_length=75)
    website2 = models.URLField(max_length=75)
    others = models.CharField(max_length=300)
    def __unicode__(self):
        return self.name


class company(models.Model):
    name = models.CharField(max_length=30)
    desc = models.CharField(max_length=300)
    person = models.ManyToManyField(person, through='company_person')
    phone1 = models.IntegerField()
    phone2_type = models.CharField(max_length=30)
    phone2 = models.IntegerField()
    phone3_type = models.CharField(max_length=30)
    phone3 = models.IntegerField()
    phone4_type = models.CharField(max_length=30)
    phone4 = models.IntegerField()
    phone5_type = models.CharField(max_length=30)
    phone5 = models.IntegerField()
    phone6_type = models.CharField(max_length=30)
    phone6 = models.IntegerField()
    email1 = models.EmailField(max_length=75)
    email2 = models.EmailField(max_length=75)
    website1 = models.URLField(max_length=75)
    email1 = models.EmailField(max_length=75)
    email2 = models.EmailField(max_length=75)
    website1 = models.URLField(max_length=75)
    website2 = models.URLField(max_length=75)


    def __unicode__(self):
        return self.name


class company_person(models.Model):
    person = models.ForeignKey(person)
    company = models.ForeignKey(company)
    desingantion = models.CharField(max_length=30)

