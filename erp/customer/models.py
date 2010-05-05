from django.db import models

class Customer(models.Model):
    name = models.CharField(max_length=100)
    details = models.TextField()
    phone_number = models.fields.PositiveIntegerField()
    email = models.fields.EmailField()
    Category = models.ForeignKey('Category')
    def __unicode__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __unicode__(self):
        return self.name



