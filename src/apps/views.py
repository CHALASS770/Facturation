from django.contrib.messages.context_processors import messages
from django.shortcuts import render
from django.views import View
from .models import *
from django.contrib import messages

class HomeView(View):
    template_name = 'index.html'
    invoices = Invoice.objects.select_related('customer', 'save_by').all()
    context = {'invoices': invoices}
    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, self.context)
    def post(self, request, *args, **kwargs):
        return render(request, self.template_name, self.context)


class AddcustomerView(View):
    template_name = 'add_customer.html'
    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)
    def post(self, request, *args, **kwargs):
        data = {
            'first_name': request.POST.get('first_name'),
            'last_name': request.POST.get('last_name'),
            'societe': request.POST.get('societe'),
            'email': request.POST.get('email'),
            'telephone': request.POST.get('telephone'),
            'Address': request.POST.get('Address'),
            'city': request.POST.get('city'),
            'save_by': request.user
        }
        print(data)
        try:
            created = Customers.objects.create(**data)
            if created:
                messages.success(request,'le client a été ajouté avec succès')
            else:
                messages.error(request,'le client n a pas été ajouté')
        except Exception as e:
            messages.error(request, f'Erreur : {e}')
        return render(request, self.template_name)

class AddinvoiceView(View):
    template_name = 'new_invoice.html'
    customers = Customers.objects.select_related('save_by').all()
    context = {
        'customers': customers
    }
    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, self.context)
    def post(self, request, *args, **kwargs):
        return render(request, self.template_name, self.context)
