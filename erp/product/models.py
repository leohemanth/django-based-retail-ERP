from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    shortcut = models.CharField(max_length=100)
    category = models.ForeignKey("Category")
    image = models.ImageField(upload_to="images")
    def __unicode__(self):
        return self.name



class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __unicode__(self):
        return self.name



