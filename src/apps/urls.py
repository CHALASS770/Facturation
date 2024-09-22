from django.urls import path
from . import views
urlpatterns = [
    path('', views.HomeView.as_view(), name ='home'),
    path('add-customer', views.AddcustomerView.as_view(), name='add-customer'),
    #path('add-customer/', views.add_customer, name='add-customer'),
    path('new-invoice', views.AddinvoiceView.as_view(), name='new-invoice'),
    #path('new-invoices/', views.add_customer, name='add-invoice'),
]