from django.db import models

class CompanyContact(models.Model):
    name = models.CharField(max_length=100)
    phone_number = models.fields.PositiveIntegerField()
    email = models.fields.EmailField()
    description = models.TextField()
    company = models.ForeignKey('Company')

    def __unicode__(self):
        return self.name

class Company(models.Model):
    name = models.CharField(max_length=100)
    details = models.TextField()
    phone_number = models.CharField(max_length=11)

    def __unicode__(self):
        return self.name
