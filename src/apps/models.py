from django.contrib.auth.models import User
from django.db import models
# Create your models here.
class Customers(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    #create a field societe not required
    societe = models.CharField(max_length=200, null=True, blank=True)
    email = models.EmailField(max_length=200)
    telephone = models.CharField(max_length=200)
    Address = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    date_created = models.DateTimeField(auto_now_add=True)
    save_by = models.ForeignKey(User, on_delete=models.PROTECT)

    class Meta:
        verbose_name = "Customer"
        verbose_name_plural = "Customers"
    def __str__(self):
        #return firstnam et lastname
        return f"{self.first_name} {self.last_name}"



class Invoice(models.Model):
    INVOICES_TYPE = (
        ('facture', 'FACTURE'),
        ('devis', 'DEVIS'),
        ('Proforma', 'Proforma'),
    )
    customer = models.ForeignKey(Customers, on_delete=models.PROTECT)
    date_created = models.DateTimeField(auto_now_add=True)
    date_due = models.DateTimeField()
    date_paid = models.DateTimeField(null=True, blank=True)
    amount = models.DecimalField(max_digits=10000, decimal_places=2)
    status = models.BooleanField(default=True)
    save_by = models.ForeignKey(User, on_delete=models.PROTECT)
    invoice_type = models.CharField(max_length=200 , choices=INVOICES_TYPE, default='facture')
    class Meta:
        verbose_name = "Invoice"
        verbose_name_plural = "Invoices"
    def __str__(self):
        return f"{self.customer.first_name} {self.customer.last_name} - {self.amount} - {self.date_created}"
    @property
    def get_amount(self):
        #return total amount of invoice
        return sum(item.get_amount for item in self.invoiceitem_set.all())

class InvoiceItem(models.Model):
    invoice = models.ForeignKey(Invoice, on_delete=models.CASCADE)
    description = models.CharField(max_length=200)
    quantity = models.IntegerField()
    price = models.DecimalField(max_digits=10000, decimal_places=2)
    #reduction is in pourcentage max is 50% it's mean integer from 0 by default to 50
    reduction = models.IntegerField(default=0)
    amount = models.DecimalField(max_digits=10000, decimal_places=2)
    class Meta:
        verbose_name = "Invoice Item"
        verbose_name_plural = "Invoice Items"
    def __str__(self):
        return f"{self.invoice.customer.first_name} {self.invoice.customer.last_name} - {self.description} - {self.amount}"
    @property
    def get_amount(self):
        #return total amount quantity * price - redutcion in pourcentage
        return self.quantity * self.price - (self.quantity * self.price * self.reduction / 100)