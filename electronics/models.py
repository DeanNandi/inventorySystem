from django.db import models


class Electronics(models.Model):
    Type = models.CharField(max_length=255)
    Model = models.CharField(max_length=255)
    Serial = models.CharField(max_length=255)
    assignment = models.CharField(max_length=255)

    class Meta:
        abstract = True


class Phones(Electronics):
    pass


class Tablets(Electronics):
    pass


class Laptops(Electronics):
    pass


class Pcs(Electronics):
    pass


class Device(models.Model):
    Name = models.CharField(max_length=255)
    Type = models.CharField(max_length=255)
    Model = models.CharField(max_length=255)
    Serial = models.CharField(max_length=255)
    assignment = models.CharField(max_length=255)


class Procurements(models.Model):
    Item = models.CharField(max_length=2555)
    Number = models.IntegerField(max_length=255)
    Date = models.CharField(max_length=255)
    Location = models.CharField(max_length=255)


class Donors(models.Model):
    Name = models.CharField(max_length=2555)
    email = models.EmailField()
    Items_supplied = models.TextField(max_length=2555)
    quantity = models.CharField(max_length=255)
    date = models.CharField(max_length=255)


class Suppliers(models.Model):
    Name = models.CharField(max_length=2555)
    email = models.EmailField()
    Items_supplied = models.TextField(max_length=2555)
    quantity = models.CharField(max_length=255)
    date = models.CharField(max_length=255)


class Purchases(models.Model):
    Name = models.CharField(max_length=2555)
    Quantity = models.CharField(max_length=2555)
    Price = models.CharField(max_length=255)
    Supplier = models.CharField(max_length=2555)
    date = models.CharField(max_length=255)


class Issuing(models.Model):
    Name = models.CharField(max_length=2555)
    Issued_to = models.CharField(max_length=255)
    Quantity = models.CharField(max_length=255)
    date = models.CharField(max_length=255)

