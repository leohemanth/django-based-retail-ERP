from django.db import models
from erp.product.models import *

class invoice(models.Model):
    customer_name = models.CharField(max_length=30)
    address = models.CharField(max_length=30)
    invoice_no = models.AutoField(primary_key=True)
    date = models.DateField()
    time = models.TimeField()

    def __unicode__(self):
        return self.customer_name

class sale(models.Model):
    product = models.ManyToManyField(product)
    quantity = models.IntegerField()

    def __unicode__(self):
        return self.id