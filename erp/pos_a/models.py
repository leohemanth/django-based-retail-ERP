from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    shortcut = models.CharField(max_length=100)
    category = models.ForeignKey("Category")
    def __unicode__(self):
        return self.name


class ProductPrice(models.Model):
    product = models.ForeignKey(Product)
    selling_price = models.DecimalField(max_digits=7,decimal_places=2)
    datetime = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-datetime']

    def __unicode__(self):
        return self.product.name


class PurchaseInvoice(models.Model):
    company = models.ForeignKey('Company')
    datetime = models.DateTimeField()

    def __unicode__(self):
        return str(self.id)


class Payment(models.Model):
    mode_choices = ((1,'Cheque'),
                    (2,'Cash'),
                    (3,'DD'))
    mode = models.PositiveSmallIntegerField(choices=mode_choices)
    description = models.TextField()
    invoice = models.ForeignKey(PurchaseInvoice)

    def __unicode__(self):
        return str(self.mode)


class PurchaseInvoiceItem(models.Model):
    invoice = models.ForeignKey(PurchaseInvoice)
    product = models.ForeignKey(Product)
    quantity = models.PositiveSmallIntegerField()
    price = models.DecimalField(max_digits=7,decimal_places=2)
    cost_price = models.DecimalField(max_digits=7,decimal_places=2)

    def __unicode__(self):
        return "%s:%s:%s"%(self.invoice.id,self.product.name,self.quantity)



class SaleInvoice(models.Model):
    customer = models.ForeignKey('Customer')
    datetime = models.DateTimeField(auto_now=True)
    def __unicode__(self):
        return str(self.pk)

class SaleInvoiceItem(models.Model):
    invoice = models.ForeignKey(SaleInvoice)
    product = models.ForeignKey(Product)
    quantity = models.PositiveSmallIntegerField()
    sold_at_price = models.DecimalField(max_digits=7,decimal_places=2)

    def __unicode__(self):
        return "%s:%s"%(self.invoice.id,self.product.name)

class CompanyContact(models.Model):
    name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=11)
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

class Customer(models.Model):
    name = models.CharField(max_length=100)
    details = models.TextField()
    phone_number = models.CharField(max_length=11)

    def __unicode__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __unicode__(self):
        return self.name



