from django import forms
from .models import Laptops, Phones, Pcs, Tablets, Device, Procurements, Donors, Suppliers, Purchases, Issuing
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model


class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField(help_text='A valid email address, please.', required=True)

    class Meta:
        model = get_user_model()
        fields = ['first_name', 'last_name', 'username', 'email', 'password1', 'password2']

    def save(self, commit=True):
        user = super(UserRegistrationForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user


class DonorsForm(forms.ModelForm):
    class Meta:
        model = Donors
        fields = ('Name', 'email', 'Items_supplied', 'quantity', 'date')
        labels = {'Name': 'Name Of Donor', 'email': 'Email Of Donor', 'Items_supplied': 'Items Supplied',
                  'quantity': 'Quantity', 'date': 'Date Received'}


class SuppliersForm(forms.ModelForm):
    class Meta:
        model = Suppliers
        fields = ('Name', 'email', 'Items_supplied', 'quantity', 'date')
        labels = {'Name': 'Name Of Supplier', 'email': 'Email Of Supplier', 'Items_supplied': 'Items Supplied',
                  'quantity': 'Quantity', 'date': 'Date Received'}


class PurchasesForm(forms.ModelForm):
    class Meta:
        model = Purchases
        fields = ('Name', 'Quantity', 'Price', 'Supplier', 'date')
        labels = {'Name': 'Name Of Item', 'Quantity': 'Quantity of Items', 'Price': 'Total Price of Items', 'Supplier': 'Bought From',
                  'date': 'Date Received'}


class IssuesForm(forms.ModelForm):
    class Meta:
        model = Issuing
        fields = ('Name', 'Issued_to', 'Quantity', 'date')
        labels = {'Name': 'Name Of Item', 'Issued_to': 'Issued To', 'Quantity': 'Amount Given', 'date': 'Date Issued'}


class ProcurementsForm(forms.ModelForm):
    class Meta:
        model = Procurements
        fields = ('Item', 'Number', 'Date', 'Location')
        labels = {'Item': 'Name Of Item', 'Number': 'Number Purchased', 'Date': 'Procurement Date',
                  'Location': 'Where Assigned'}


class LaptopForm(forms.ModelForm):
    class Meta:
        model = Laptops
        fields = ('Type', 'Model', 'Serial', 'assignment')
        labels = {'Type': 'Item name', 'Model': 'Model Of Gadget', 'Serial': 'Serial No',
                  'assignment': 'Assigned To'}


class PhonesForm(forms.ModelForm):
    class Meta:
        model = Phones
        fields = ('Type', 'Model', 'Serial', 'assignment')
        labels = {'Type': 'Item name', 'Model': 'Model Of Gadget', 'Serial': 'Serial No',
                  'assignment': 'Assigned To'}


class PcsForm(forms.ModelForm):
    class Meta:
        model = Pcs
        fields = ('Type', 'Model', 'Serial', 'assignment')
        labels = {'Type': 'Item name', 'Model': 'Model Of Gadget', 'Serial': 'Serial No',
                  'assignment': 'Assigned To'}


class TabletsForm(forms.ModelForm):
    class Meta:
        model = Tablets
        fields = ('Type', 'Model', 'Serial', 'assignment')
        labels = {'Type': 'Item name', 'Model': 'Model Of Gadget', 'Serial': 'Serial No',
                  'assignment': 'Assigned To'}


class DeviceForm(forms.ModelForm):
    class Meta:
        model = Device
        fields = ('Name','Type', 'Model', 'Serial', 'assignment')
        labels = {'Name': 'Item Name','Type': 'Item Type', 'Model': 'Model Of Gadget', 'Serial': 'Serial No',
                  'assignment': 'Assigned To'}