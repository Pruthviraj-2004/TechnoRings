from django import views
from django.urls import path
from .views import *
from . import views

urlpatterns = [

    path('home/', views.home, name='home'),

    path('add-transport-order/', TransportOrderView.as_view(), name='add_transport_order'),
    path('service-order/', ServiceOrderView.as_view(), name='service-order'),
    path('generate_bill/<int:service_order_id>/', GenerateBillView.as_view(), name='generate_bill'),
    path('store-delivery-challan/', StoreDeliveryChallan.as_view(), name='store_delivery_challan'),

    path('instrument-tools/', InstrumentToolsView.as_view(), name='instrument_tools'),
    path('instrument-family-group-tools/', InstrumentFamilyGroupView.as_view(), name='instrument_family_group_tools'),
    path('instrument-group-master-tools/', InstrumentGroupMasterView.as_view(), name='instrument_group_master_tools'),
    path('instrument-service-tools/', InstrumentServiceToolsView.as_view(), name='instrument_service_tools'),
    path('shed-details/', ShedDetailsView.as_view(), name='shed_details'),
    path('shed-tools/', ShedToolsView.as_view(), name='shed_tools'),
    path('shed_detail/<int:shed_id>/', ShedDetailAPIView.as_view(), name='api_shed_detail'),
    path('vendor_types/', VendorTypeView.as_view(), name='vendor_type'),
    path('vendor/', VendorView.as_view(), name='vendor'),
    path('vendor_handles/', VendorHandlesView.as_view(), name='vendor_handles'),
    path('vendor_details/<int:vendor_id>/', VendorDetailsView1.as_view(), name='vendor_details'),
    path('service_types/', ServiceTypeView.as_view(), name='service-type-list'),

    path('instrument-transport-history/<int:instrument_id>/', InstrumentTransportHistoryView.as_view(), name='instrument_transport_history'),
    path('instrument-service-history/<int:instrument_id>/', InstrumentServiceHistoryView.as_view(), name='instrument_service_history'),
    path('instrument-calibration-history/<int:instrument_id>/', InstrumentCalibrationHistoryView.as_view(), name='instrument-calibration-history'),

    path('transport_orders/<int:movement_id>/', TransportOrderViews.as_view(), name='transport_order_detail'),
    path('service_orders/<int:service_id>/', ServiceOrderViews.as_view(), name='service_order_detail'),
    path('delivery-challans/<int:deliverychallan_id>/', DeliveryChallanViews.as_view(), name='delivery-challan-detail'),
    path('calibration_reports/', CalibrationReportView.as_view(), name="all-calibration-reports"),

    path('add_instrument1/', AddInstrumentModelView1.as_view(), name='add_instrument1'),
    path('add_instrument_group_master/', AddInstrumentGroupMasterView.as_view(), name='add_instrument_group_master'),
    path('add_instrument_family/', AddInstrumentFamilyView.as_view(), name='add_instrument_family'),
    path('add_shed/', AddShedDetailsView.as_view(), name='add_shed_details'),
    path('add_shed_tools/', AddShedToolsView.as_view(), name='add_shed_tools'),
    path('add_vendor/', AddVendorView.as_view(), name='add_vendor'),
    path('add_vendor_handles/', AddVendorHandlesView.as_view(), name='add_vendor_handles'),

    path('update_shed/<int:shed_id>/', UpdateShedDetailsView.as_view(), name='update_shed'),


    path('vendor/<int:vendor_id>/delete/', VendorDeleteView.as_view(), name='vendor_delete'),
    path('shed/<int:shed_id>/delete/', ShedDeleteView.as_view(), name='delete_shed'),
    path('transport_order/<int:movement_id>/delete/', TransportOrderDeleteView.as_view(), name='delete_transport_order'),
    path('service_order/<int:service_id>/delete/', ServiceOrderDeleteView.as_view(), name='service_order_delete'),
    path('delivery_challan/<int:delivery_challan_id>/delete/', DeleteDeliveryChallanView.as_view(), name='delete_delivery_challan'),
    path('calibration_report/<int:calibration_report_id>/delete/', DeleteCalibrationReportView.as_view(), name='delete_calibration_report'),
    path('shed_tool/<int:shedtool_id>/delete/', DeleteShedToolsView.as_view(), name='delete_shed_tool'),
    path('transport_tool/<int:transporttool_id>/delete/', DeleteTransportToolsView.as_view(), name='delete_transport_tool'),
    path('service_tool/<int:servicetool_id>/delete/', DeleteServiceToolsView.as_view(), name='delete_service_tool'),
    path('delivery_challan_tool/<int:deliverychallantool_id>/delete/', DeleteDeliveryChallanToolsView.as_view(), name='delete_delivery_challan_tool'),
    path('vendor_handles/<int:vendorhandle_id>/delete/', DeleteVendorHandlesView.as_view(), name='delete_vendor_handles'),
    path('instrument_group/<int:tool_id>/delete/', DeleteInstrumentGroupMasterView.as_view(), name='delete_instrument_group'),
    path('instrument_family/<int:instrumentfamilyid>/delete/', DeleteInstrumentFamilyGroupView.as_view(), name='delete_instrument_family_group'),
    path('instrument/<int:instrument_no>/delete/', DeleteInstrumentModelView.as_view(), name='delete_instrument_model'),

    path('transport/<int:order_id>/acknowledge/', TransportAcknowledgmentView.as_view(), name='transport_acknowledge'),
    path('transport_acknowledge_tools/<int:order_id>/', TransportAcknowledgmentToolsView.as_view(), name='transport_acknowledge_tools'),
    # path('update-service-status/', update_service_status, name='update_service_status'),

    path('all_transport_orders/', AllTransportOrderView.as_view(), name='all-transport-orders'),
    path('recent_transport_orders/', RecentTransportOrderView.as_view(), name='recent-transport-orders'),
    path('all_service_orders/', AllServiceOrderView.as_view(), name='all-service-orders'),
    path('recent_service_orders/', RecentServiceOrderView.as_view(), name='recent-service-orders'),
    path('all_delivery_challan/', AllDeliveryChallanView.as_view(), name='all-delivery-challan'),
    path('recent_delivery_challan/', RecentDeliveryChallanView.as_view(), name='recent-delivery-challan'),
    
    path('count_of/', CountOfObjects.as_view(), name='count_of'),

    path('update_instrument_shed/', UpdateInstrumentShedView.as_view(), name='update_instrument_shed'),

    path('instruments_by_tool_group/<int:tool_group_id>/', InstrumentsByGroupView.as_view(), name='instruments-by-group'),
    path('pending-service-orders/vendor/<int:vendor_id>/', PendingServiceOrdersByVendorView.as_view(), name='pending-service-orders-by-vendor'),

    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),

]