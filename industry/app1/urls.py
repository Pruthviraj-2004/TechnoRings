from django import views
from django.urls import path
from .views import GenerateBillView, InstrumentToolsView,  ServiceOrderView, ShedDetailsView, ShedToolsView, TransportOrderView, VendorHandlesView#, ServiceOrderClass, ServiceToolsClass, TransportMovementOrderClass,TransportToolsClass
from . import views

urlpatterns = [
    # path('transport-movement/', TransportMovementOrderClass.as_view(), name='transport_movement'),
    # path('transport-tools/', TransportToolsClass.as_view(), name='transport_tools'),
    # path('service-tools/', ServiceToolsClass.as_view(), name='service_tools'),
    # path('service-order/', ServiceOrderClass.as_view(), name='service_order'),
    path('home/', views.home, name='home'),
    path('add-transport-order/', TransportOrderView.as_view(), name='add_transport_order'),
    path('service-order/', ServiceOrderView.as_view(), name='service-order'),
    path('generate-bill/', GenerateBillView.as_view(), name='generate_bill'),
    #path('create_delivery_challan/', views.CreateDeliveryChallanView.as_view(), name='create_delivery_challan'),
    path('delivery_challan/', views.DeliveryChallanView.as_view(), name='delivery_challan'),

    path('instrument-tools/', InstrumentToolsView.as_view(), name='instrument_tools'),
    path('shed-details/', ShedDetailsView.as_view(), name='shed_details'),
    path('shed-tools/', ShedToolsView.as_view(), name='shed_tools'),
    path('vendor-handles/', VendorHandlesView.as_view(), name='vendor_handles'),


]