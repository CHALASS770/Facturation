from django.contrib import admin
from .models import *
# Register your models here.
class AdminCustomer(admin.ModelAdmin):
    list_display = ['first_name','last_name','email','telephone','Address','city','date_created','save_by']
    search_fields = ['first_name','last_name','email','telephone','Address','city','date_created','save_by']
    list_filter = ['first_name','last_name','email','telephone','Address','city','date_created','save_by']
    list_per_page = 10
class AdminInvoice(admin.ModelAdmin):
    list_display = ['customer','date_created','date_due','date_paid','amount','status','save_by','invoice_type']
    search_fields = ['customer','date_created','date_due','date_paid','amount','status','save_by','invoice_type']
    list_filter = ['customer','date_created','date_due','date_paid','amount','status','save_by','invoice_type']
    list_per_page = 10
admin.site.register(Customers,AdminCustomer)
admin.site.register(Invoice,AdminInvoice)
admin.site.register(InvoiceItem)