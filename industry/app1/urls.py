from django import views
from django.urls import path
from .views import AddInstrumentFamilyView, AddInstrumentGroupMasterView, AddInstrumentModelView1, AddInstrumentView, AddShedDetailsView, AddShedToolsView, AddVendorHandlesView, AddVendorView, DeleteCalibrationReportView, DeleteDeliveryChallanView, GenerateBillView, InstrumentFamilyGroupView, InstrumentGroupMasterView, InstrumentServiceHistoryView, InstrumentToolsView, InstrumentTransportHistoryView, ServiceOrderDeleteView,  ServiceOrderView, ShedDeleteView, ShedDetailAPIView, ShedDetailView1, ShedDetailsView, ShedToolsView, TransportOrderDeleteView, TransportOrderView, VendorDeleteView, VendorDetailsView1, VendorView
from . import views

urlpatterns = [

    path('home/', views.home, name='home'),

    path('add-transport-order/', TransportOrderView.as_view(), name='add_transport_order'),
    path('service-order/', ServiceOrderView.as_view(), name='service-order'),
    path('generate_bill/<int:service_order_id>/', GenerateBillView.as_view(), name='generate_bill'),
    path('delivery_challan/', views.DeliveryChallanView.as_view(), name='delivery_challan'),

    path('instrument-tools/', InstrumentToolsView.as_view(), name='instrument_tools'),
    path('instrument-family-group-tools/', InstrumentFamilyGroupView.as_view(), name='instrument_family_group_tools'),
    path('instrument-group-master-tools/', InstrumentGroupMasterView.as_view(), name='instrument_group_master_tools'),


    path('shed-details/', ShedDetailsView.as_view(), name='shed_details'),
    path('shed-tools/', ShedToolsView.as_view(), name='shed_tools'),
    path('vendor/', VendorView.as_view(), name='vendor'),
    path('shed/<int:shed_id>/', ShedDetailView1.as_view(), name='shed_detail'),
    path('shed_detail/<int:shed_id>/', ShedDetailAPIView.as_view(), name='api_shed_detail'),
    path('vendor_details/<int:vendor_id>/', VendorDetailsView1.as_view(), name='vendor_details'),

    path('instrument-transport-history/<int:instrument_id>/', InstrumentTransportHistoryView.as_view(), name='instrument_transport_history'),
    path('instrument-service-history/<int:instrument_id>/', InstrumentServiceHistoryView.as_view(), name='instrument_service_history'),

    path('add_instrument/', AddInstrumentView.as_view(), name='add_instrument'),
    path('add_instrument1/', AddInstrumentModelView1.as_view(), name='add_instrument1'),
    path('add_instrument_group_master/', AddInstrumentGroupMasterView.as_view(), name='add_instrument_group_master'),
    path('add_instrument_family/', AddInstrumentFamilyView.as_view(), name='add_instrument_family'),
    path('add_shed/', AddShedDetailsView.as_view(), name='add_shed_details'),
    path('add_shed_tools/', AddShedToolsView.as_view(), name='add_shed_tools'),
    path('add_vendor/', AddVendorView.as_view(), name='add_vendor'),
    path('add_vendor_handles/', AddVendorHandlesView.as_view(), name='add_vendor_handles'),

    path('vendor/<int:vendor_id>/delete/', VendorDeleteView.as_view(), name='vendor_delete'),
    path('shed/<int:shed_id>/delete/', ShedDeleteView.as_view(), name='delete_shed'),
    path('transport_order/<int:movement_id>/delete/', TransportOrderDeleteView.as_view(), name='delete_transport_order'),
    # path('service_order/<int:service_id>/delete/', ServiceOrderDeleteView.as_view(), name='service_order_delete'),
    path('delivery_challan/<int:delivery_challan_id>/delete/', DeleteDeliveryChallanView.as_view(), name='delete_delivery_challan'),
    path('calibration_report/<int:calibration_report_id>/delete/', DeleteCalibrationReportView.as_view(), name='delete_calibration_report'),

]