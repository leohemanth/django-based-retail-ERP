from django.db import models



class SaleInvoice(models.Model):
    customer = models.ForeignKey('customer.Customer')
    datetime = models.DateTimeField(auto_now=True)
    
    def __unicode__(self):
        return str(self.pk)

    
class SaleInvoiceItem(models.Model):
    invoice = models.ForeignKey(SaleInvoice)
    product = models.ForeignKey('product.Product')
    quantity = models.PositiveSmallIntegerField()
    sold_at_price = models.DecimalField(max_digits=7,decimal_places=2)

    def __unicode__(self):
        return "%s:%s"%(self.invoice.id,self.product.name)


