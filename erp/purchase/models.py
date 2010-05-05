from django.db import models


class PurchaseInvoice(models.Model):
    company = models.ForeignKey('company.Company')
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
    product = models.ForeignKey('product.Product')
    quantity = models.PositiveSmallIntegerField()
    price = models.DecimalField(max_digits=7,decimal_places=2)
    cost_price = models.DecimalField(max_digits=7,decimal_places=2)

    def __unicode__(self):
        return "%s:%s:%s"%(self.invoice.id,self.product.name,self.quantity)

