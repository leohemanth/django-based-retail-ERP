from django.db import models

class group(models.Model):
    name = models.CharField(max_length=30)
    desc = models.CharField(max_length=300)
    def __unicode__(self):
        return self.name


class product(models.Model):
    name = models.CharField(max_length=30)
    desc = models.CharField(max_length=300)
    group = models.ManyToManyField(group)
    def __unicode__(self):
        return self.name