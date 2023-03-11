from django.contrib import admin
from .models import Pcs, Device, Laptops, Tablets, Phones, Procurements, Suppliers, Donors, Purchases, Issuing


@admin.register(Suppliers)
class ViewAdmin(admin.ModelAdmin):
    list_display = ('Name', 'email', 'Items_supplied', 'quantity', 'date')
    pass


@admin.register(Donors)
class ViewAdmin(admin.ModelAdmin):
    list_display = ('Name', 'email', 'Items_supplied', 'quantity', 'date')
    pass


@admin.register(Purchases)
class ViewAdmin(admin.ModelAdmin):
    list_display = ('Name', 'Quantity', 'Price', 'Supplier', 'date')
    pass


@admin.register(Issuing)
class ViewAdmin(admin.ModelAdmin):
    list_display = ('Name', 'Issued_to', 'Quantity', 'date')
    pass


@admin.register(Pcs, Laptops, Tablets, Phones)
class ViewAdmin(admin.ModelAdmin):
    list_display = ('Type', 'Model', 'Serial', 'assignment')
    pass


@admin.register(Device)
class ViewAdmin(admin.ModelAdmin):
    list_display = ('Name', 'Type', 'Model', 'Serial', 'assignment')
    pass


@admin.register(Procurements)
class ViewAdmin(admin.ModelAdmin):
    list_display = ('Item', 'Number', 'Date', 'Location')
    pass

