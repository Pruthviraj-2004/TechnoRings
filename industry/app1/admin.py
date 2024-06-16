from django.contrib import admin
from .models import CalibrationReport, DeliveryChallan, DeliveryChallanTools, InstrumentFamilyGroup, InstrumentGroupMaster, InstrumentModel, ServiceType, ShedDetails, ShedTools, ServiceOrder, ServiceTools, TransportOrder, TransportTools, Vendor, VendorHandles, VendorType
from import_export.admin import ImportExportModelAdmin

@admin.register(InstrumentGroupMaster)
class InstrumentGroupMasterAdmin(ImportExportModelAdmin):
    list_display = ('tool_group_id', 'tool_group_name', 'tool_group_code')


@admin.register(InstrumentFamilyGroup)
class InstrumentFamilyGroupAdmin(ImportExportModelAdmin):
    list_display = ('instrument_family_id', 'instrument_family_name', 'instrument_group_master')
    search_fields = ('instrument_family_name',)
    list_filter = ('instrument_group_master',)

@admin.register(InstrumentModel)
class InstrumentModelAdmin(ImportExportModelAdmin):
    list_display = ('instrument_no', 'instrument_name', 'current_shed', 'type_of_tool', 'service_status', 'manufacturer_name', 'year_of_purchase', 'gst', 'description', 'instrument_range', 'least_count', 'calibration_frequency')
    list_filter = ('current_shed', 'type_of_tool', 'service_status')
    search_fields = ('instrument_name', 'current_shed')

    def get_return_instrument_names(self, obj):
        return ', '.join([i.instrument_name for i in obj.return_instruments.all()])
    get_return_instrument_names.short_description = 'Return Instruments'

    def formfield_for_manytomany(self, db_field, request, **kwargs):
        if db_field.name == 'return_instruments':
            kwargs['queryset'] = InstrumentModel.objects.exclude(pk=request.resolver_match.kwargs['object_id'])
        return super().formfield_for_manytomany(db_field, request, **kwargs)

@admin.register(ShedDetails)
class ShedDetailsAdmin(ImportExportModelAdmin):
    list_display = ('shed_id', 'name', 'location', 'phone_number')
    search_fields = ('name', 'location', 'phone_number')

@admin.register(ShedTools)
class ShedToolsAdmin(ImportExportModelAdmin):
    list_display = ('shedtool_id', 'shed', 'using_tool')
    list_filter = ('shed', 'using_tool')
    search_fields = ('shed__name', 'using_tool__instrument_name')

@admin.register(ServiceType)
class ServiceTypeAdmin(admin.ModelAdmin):
    list_display = ('servicetype_id', 'service_type')
    search_fields = ('service_type',)

@admin.register(ServiceOrder)
class ServiceOrderAdmin(ImportExportModelAdmin):
    list_display = ('service_id', 'date','vendor', 'amount', 'description', 'service_pending','created_at','updated_at')
    list_filter = ('date','service_pending')

@admin.register(ServiceTools)
class ServiceToolsAdmin(ImportExportModelAdmin):
    list_display = ('servicetool_id', 'service', 'tool', 'service_pending_tool', 'vendor','service_type')
    list_filter = ('service','vendor','service_type')

@admin.register(TransportOrder)
class TransportOrderAdmin(ImportExportModelAdmin):
    list_display = ('movement_id', 'movement_date', 'source_shed', 'destination_shed', 'acknowledgment', 'tool_count', 'created_at','updated_at')
    list_filter = ('source_shed', 'destination_shed', 'acknowledgment')
    search_fields = ('movement_id',)

@admin.register(TransportTools)
class TransportToolsAdmin(ImportExportModelAdmin):
    list_display = ('transporttool_id', 'transport', 'tool','acknowledgment')
    list_filter = ('transport','tool')
    search_fields = ('transport__movement_id', 'tool__instrument_name')

@admin.register(VendorType)
class VendorTypeAdmin(admin.ModelAdmin):
    list_display = ('vendortype_id', 'vendor_type')
    search_fields = ('vendor_type',)

@admin.register(Vendor)
class VendorAdmin(ImportExportModelAdmin):
    list_display = ('vendor_id', 'name', 'location', 'address', 'phone_number', 'email', 'nabl_number','vendor_type')
    search_fields = ('name', 'location', 'phone_number', 'email', 'nabl_number')
    list_filter = ('location',)

@admin.register(VendorHandles)
class VendorHandlesAdmin(ImportExportModelAdmin):
    list_display = ('vendorhandle_id', 'vendor_name', 'tool_id', 'turnaround_time', 'cost')
    list_filter = ('vendor', 'tool')
    search_fields = ('vendor__name', 'tool__instrument_name', 'turnaround_time')

    def vendor_name(self, obj):
        return obj.vendor.name

    vendor_name.short_description = 'Vendor Name'

    def tool_id(self, obj):
        return obj.tool.instrument_no

    tool_id.short_description = 'Tool ID'

@admin.register(DeliveryChallan)
class DeliveryChallanAdmin(ImportExportModelAdmin):
    list_display = ('deliverychallan_id', 'received_date', 'vendor', 'shed', 'service', 'created_at','updated_at')
    list_filter = ('vendor', 'shed', 'service')
    search_fields = ('deliverychallan_id', 'vendor__name')

@admin.register(DeliveryChallanTools)
class DeliveryChallanToolsAdmin(ImportExportModelAdmin):
    list_display = ('deliverychallantool_id', 'deliverychallan', 'tool','calibration_report')
    list_filter = ('deliverychallan__vendor',)
    search_fields = ('deliverychallan__vendor__name',)

@admin.register(CalibrationReport)
class CalibrationAdmin(ImportExportModelAdmin):
    list_display = ('calibrationtool_id',  'calibration_tool','calibration_date', 'calibration_report_no', 'calibration_agency', 'result', 'action', 'next_calibration_date','notification_date', 'remark')
    list_filter = ('calibration_date', 'calibration_agency', 'action', 'notification_date')
    search_fields = ('calibration_report_no', 'calibration_agency')
