from django import views
from django.urls import path
from .views import GenerateBillView, InstrumentServiceHistoryView, InstrumentToolsView, InstrumentTransportHistoryView,  ServiceOrderView, ShedDetailAPIView, ShedDetailView1, ShedDetailsView, ShedToolsView, TransportOrderView, VendorDetailsView1, VendorView
from . import views

urlpatterns = [

    path('home/', views.home, name='home'),

    path('add-transport-order/', TransportOrderView.as_view(), name='add_transport_order'),
    path('service-order/', ServiceOrderView.as_view(), name='service-order'),
    path('generate_bill/<int:service_order_id>/', GenerateBillView.as_view(), name='generate_bill'),
    path('delivery_challan/', views.DeliveryChallanView.as_view(), name='delivery_challan'),

    path('instrument-tools/', InstrumentToolsView.as_view(), name='instrument_tools'),
    path('shed-details/', ShedDetailsView.as_view(), name='shed_details'),
    path('shed-tools/', ShedToolsView.as_view(), name='shed_tools'),
    path('vendor/', VendorView.as_view(), name='vendor'),
    path('shed/<int:shed_id>/', ShedDetailView1.as_view(), name='shed_detail'),
    path('shed_detail/<int:shed_id>/', ShedDetailAPIView.as_view(), name='api_shed_detail'),
    path('vendor_details/<int:vendor_id>/', VendorDetailsView1.as_view(), name='vendor_details'),


    path('instrument-transport-history/<int:instrument_id>/', InstrumentTransportHistoryView.as_view(), name='instrument_transport_history'),
    path('instrument-service-history/<int:instrument_id>/', InstrumentServiceHistoryView.as_view(), name='instrument_service_history'),


]