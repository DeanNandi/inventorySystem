from django.urls import path
from . import views


urlpatterns = [
    path('stock-collection', views.stock, name='stock-collection'),
    path('suppliers-report', views.suppliers_reports, name='suppliers-report'),
    path('purchases-report', views.purchases_reports, name='purchases-report'),
    path('donors-report', views.donors_reports, name='donors-report'),
    path('issuing-report', views.issued_out_reports, name='issuing-report'),
    path("register", views.registerPage, name="register"),
    path('login', views.loginPage, name='login'),
    path('logout', views.logoutUser, name='logout'),


    path('', views.landing_page),
    path('supplies-page', views.supplies, name='supplies-page'),
    path('reports', views.index, name='reports'),
    path('landing-page', views.landing_page, name='landing-page'),
    path('gadgets-page', views.gadgets_page, name='gadgets-page'),
    path('laptop-reports', views.laptop_reports, name='laptop-reports'),
    path('phone-reports', views.phone_reports, name='phone-reports'),
    path('pcs-reports', views.pcs_reports, name='pcs-reports'),
    path('devices-reports', views.devices_reports, name='devices-reports'),
    path('tablets-reports', views.tablets_reports, name='tablets-reports'),
    path('procurements-reports', views.procurements_reports, name='procurements-reports'),

    path('display-procurements', views.display_procurements, name='display-procurements'),
    path('display-laptops', views.display_laptops, name='display-laptops'),
    path('display-pcs', views.display_pcs, name='display-pcs'),
    path('display-devices', views.display_device, name='display-devices'),
    path('display-tablets', views.display_tablets, name='display-tablets'),
    path('display-phones', views.display_phones, name='display-phones'),

    path('add-new-procurement', views.add_procurement, name='add-new-procurement'),
    path('add-new-laptops', views.add_laptop, name='add-new-laptops'),
    path('add-new-phones', views.add_phones, name='add-new-phones'),
    path('add-new-pcs', views.add_pcs, name='add-new-pcs'),
    path('add-new-tablets', views.add_tablets, name='add-new-tablets'),
    path('add-new-devices', views.add_device, name='add-new-devices'),

    path('update-suppliers', views.add_suppliers, name='update-suppliers'),
    path('update-donors', views.add_donors, name='update-donors'),
    path('update-purchases', views.add_purchases, name='update-purchases'),
    path('update-issuing', views.add_issuing, name='update-issuing'),

    path('edit-procurements/(?P<pk>\d+)', views.edit_procurement, name='edit-procurements/(?P<pk>\d+)'),
    path('edit-laptops/(?P<pk>\d+)', views.edit_laptop, name='edit-laptops/(?P<pk>\d+)'),
    path('edit-phones/(?P<pk>\d+)', views.edit_phones, name='edit-phones/(?P<pk>\d+)'),
    path('edit-pcs/(?P<pk>\d+)', views.edit_pcs, name='edit-pcs/(?P<pk>\d+)'),
    path('edit-tablets/(?P<pk>\d+)', views.edit_tablets, name='edit-tablets/(?P<pk>\d+)'),
    path('edit-devices/(?P<pk>\d+)', views.edit_devices, name='edit-devices/(?P<pk>\d+)'),

    path('delete-procurement/(?P<pk>\d+)', views.delete_procurements, name='delete-procurement/(?P<pk>\d+)'),
    path('delete-laptop/(?P<pk>\d+)', views.delete_laptop, name='delete-laptop/(?P<pk>\d+)'),
    path('delete-pcs/(?P<pk>\d+)', views.delete_pcs, name='delete-pcs/(?P<pk>\d+)'),
    path('delete-other-device/(?P<pk>\d+)', views.delete_other_devices, name='delete-other-device/(?P<pk>\d+)'),
    path('delete-tablet/(?P<pk>\d+)', views.delete_other_devices, name='delete-tablet/(?P<pk>\d+)'),
    path('delete-phones/(?P<pk>\d+)', views.delete_phones, name='delete-phones/(?P<pk>\d+)'),

]