from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import Electronics, Laptops, Phones, Pcs, Tablets, Device, Procurements, Donors, Suppliers, Purchases, \
    Issuing
from .forms import LaptopForm, PhonesForm, PcsForm, TabletsForm, DeviceForm, ProcurementsForm, DonorsForm, SuppliersForm, \
                   PurchasesForm, IssuesForm
from django.contrib.auth import get_user_model, login, authenticate
from .forms import UserRegistrationForm
from django.contrib import messages
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm


def register(request):
    # Logged in user can't register a new account
    if request.user.is_authenticated:
        return redirect("http://127.0.0.1:8000/landing-page")

    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, f"New account created: {user.username}")
            return redirect('http://127.0.0.1:8000/landing-page')
        else:
            for error in list(form.errors.values()):
                messages.error(request, error)

    else:
        form = UserRegistrationForm()

    return render(
        request = request,
        template_name = "register.html",
        context={"form":form}
        )


@login_required
def custom_logout(request):
    logout(request)
    return redirect("http://127.0.0.1:8000/landing-page")


def custom_login(request):
    if request.user.is_authenticated:
        return redirect('http://127.0.0.1:8000/landing-page')

    if request.method == 'POST':
        form = AuthenticationForm(request=request, data=request.POST)
        if form.is_valid():
            user = authenticate(
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password'],
            )
            if user is not None:
                login(request, user)

                return redirect('http://127.0.0.1:8000/landing-page')

        else:
            for error in list(form.errors.values()):
                messages.error(request, error)

    form = AuthenticationForm()

    return render(
        request=request,
        template_name="login.html",
        context={'form': form}
    )


def stock(request):
    return render(request, 'stock.html', {})


def issued_out_reports(request):
    issuing = Issuing.objects.all()
    return render(request, 'issuedreport.html', {'issuing':issuing})


def donors_reports(request):
    donors = Donors.objects.all()
    return render(request, 'donors.html', {'donors': donors})


def suppliers_reports(request):
    suppliers = Suppliers.objects.all()
    return render(request, 'suppliers.html', {'suppliers': suppliers})


def purchases_reports(request):
    purchases = Purchases.objects.all()
    return render(request, 'purchases.html', {'purchases': purchases})


def laptop_reports(request):
    laptops = Laptops.objects.all()
    return render(request, 'lapreports.html', {'laptops': laptops})


def phone_reports(request):
    phones = Phones.objects.all()
    return render(request, 'phonereports.html', {'phones': phones})


def pcs_reports(request):
    pcs = Pcs.objects.all()
    return render(request, 'pcsreports.html', {'pcs': pcs})


def devices_reports(request):
    devices = Device.objects.all()
    return render(request, 'devicereports.html', {'devices': devices})


def tablets_reports(request):
    tablets = Tablets.objects.all()
    return render(request, 'tabreports.html', {'tablets': tablets})


def procurements_reports(request):
    procurements = Procurements.objects.all()
    return render(request, 'procreports.html', {'procurements': procurements})


def supplies(request):
    return render(request, 'supplies.html', {})


def index(request):
    return render(request, 'index.html', {})


def test(request):
    return render(request, 'test.html', {})


def gadgets_page(request):
    return render(request, 'gadgets.html',{})


def landing_page(request):

    return render(request, 'landing-page.html', {})


def display_procurements(request):
    items = Procurements.objects.all()
    context = {
        'items': items,
        'header': 'Procurements',

    }
    return render(request, 'procurements.html', context)


def display_laptops(request):
    items = Laptops.objects.all()
    context = {
        'items': items,
        'header': 'Laptops',

    }
    return render(request, 'laptops.html', context)


def display_pcs(request):
    items = Pcs.objects.all()
    context = {
        'items': items,
        'header': 'Pcs'
    }
    return render(request, 'pcs.html', context)


def display_device(request):
    items = Device.objects.all()
    context = {
        'items': items,
        'header': 'Device'

    }
    return render(request, 'otherdevice.html', context)


def display_tablets(request):
    items = Tablets.objects.all()
    context = {
        'items': items,
        'header': 'Tablets'

    }
    return render(request, 'tablets.html', context)


def display_phones(request):
    items = Phones.objects.all()
    context = {
        'items': items,
        'header': 'Phones'

    }
    return render(request, 'phones.html', context)


def add_new(request, cls):
    if request.method == "POST":
        form = cls(request.POST)

        if form.is_valid():
            form.save()
            return redirect('http://127.0.0.1:8000/electronics/supplies-page')

    else:
        form = cls()
        return render(request, 'add_new.html', {'form': form})


def add_donors(request):
    return add_new(request, DonorsForm)


def add_suppliers(request):
    return add_new(request, SuppliersForm)


def add_purchases(request):
    return add_new(request, PurchasesForm)


def add_issuing(request):
    return add_new(request, IssuesForm)


def add_item(request, cls):
    if request.method == "POST":
        form = cls(request.POST)

        if form.is_valid():
            form.save()
            return redirect('http://127.0.0.1:8000/electronics/gadgets-page')

    else:
        form = cls()
        return render(request, 'add_new.html', {'form': form})


def add_procurement(request):
    return add_item(request, ProcurementsForm)


def add_laptop(request):
    return add_item(request, LaptopForm)


def add_phones(request):
    return add_item(request, PhonesForm)


def add_pcs(request):
    return add_item(request, PcsForm)


def add_tablets(request):
    return add_item(request, TabletsForm)


def add_device(request):
    return add_item(request, DeviceForm)


def edit_item(request, pk, model, cls):
    item = get_object_or_404(model, pk=pk)

    if request.method == "POST":
        form = cls(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect('http://127.0.0.1:8000/electronics/landing-page')
    else:
        form = cls(instance=item)

        return render(request, 'edit_item.html', {'form': form})


def edit_procurement(request, pk):
    return edit_item(request, pk, Procurements, ProcurementsForm)


def edit_laptop(request, pk):
    return edit_item(request, pk, Laptops, LaptopForm)


def edit_phones(request, pk):
    return edit_item(request, pk, Phones, PhonesForm)


def edit_pcs(request, pk):
    return edit_item(request, pk, Pcs, PcsForm)


def edit_tablets(request, pk):
    return edit_item(request, pk, Tablets, TabletsForm)


def edit_devices(request, pk):
    return edit_item(request, pk, Device, DeviceForm)


def delete_procurements(request, pk):
    template = 'procurements.html'
    Procurements.objects.filter(id=pk).delete()

    items = Procurements.objects.all()

    context = {
        'items': items,
    }

    return render(request, template, context)


def delete_laptop(request, pk):

    template = 'laptops.html'
    Laptops.objects.filter(id=pk).delete()

    items = Laptops.objects.all()

    context = {
        'items': items,
    }

    return render(request, template, context)


def delete_pcs(request, pk):

    template = 'pcs.html'
    Pcs.objects.filter(id=pk).delete()

    items = Pcs.objects.all()

    context = {
        'items': items,
    }

    return render(request, template, context)


def delete_other_devices(request, pk):

    template = 'otherdevice.html'
    Device.objects.filter(id=pk).delete()

    items = Device.objects.all()

    context = {
        'items': items,
    }

    return render(request, template, context)


def delete_tablets(request, pk):

    template = 'tablets.html'
    Tablets.objects.filter(id=pk).delete()

    items = Tablets.objects.all()

    context = {
        'items': items,
    }

    return render(request, template, context)


def delete_phones(request, pk):

    template = 'phones.html'
    Phones.objects.filter(id=pk).delete()

    items = Phones.objects.all()

    context = {
        'items': items,
    }

    return render(request, template, context)

