from django.contrib import admin
from .models import CalibrationReport, DeliveryChallan, DeliveryChallanTools, InstrumentFamilyGroup, InstrumentGroupMaster, InstrumentModel, ShedDetails, ShedTools, ServiceOrder, ServiceTools, TransportOrder, TransportTools, Vendor, VendorHandles


@admin.register(InstrumentGroupMaster)
class InstrumentGroupMasterAdmin(admin.ModelAdmin):
    list_display = ('tool_group_name', 'tool_group_code', 'instrument_type')

@admin.register(InstrumentFamilyGroup)
class InstrumentFamilyGroupAdmin(admin.ModelAdmin):
    list_display = ('instrumentfamilyid', 'instrument_family_name', 'instrument_group_master')
    search_fields = ('instrument_family_name',)
    list_filter = ('instrument_group_master',)

@admin.register(InstrumentModel)
class InstrumentModelAdmin(admin.ModelAdmin):
    list_display = ('instrument_no', 'instrument_name', 'manufacturer_name', 'year_of_purchase', 'gst', 'description', 'instrument_range', 'least_count', 'type_of_tool', 'calibration_frequency')
    list_filter = ('manufacturer_name', 'year_of_purchase', 'type_of_tool', 'calibration_frequency')
    search_fields = ('instrument_name', 'manufacturer_name', 'description')

    def get_return_instrument_names(self, obj):
        return ', '.join([i.instrument_name for i in obj.return_instruments.all()])
    get_return_instrument_names.short_description = 'Return Instruments'

    def formfield_for_manytomany(self, db_field, request, **kwargs):
        if db_field.name == 'return_instruments':
            kwargs['queryset'] = InstrumentModel.objects.exclude(pk=request.resolver_match.kwargs['object_id'])
        return super().formfield_for_manytomany(db_field, request, **kwargs)

@admin.register(ShedDetails)
class ShedDetailsAdmin(admin.ModelAdmin):
    list_display = ('shed_id', 'name', 'location', 'phone_number')
    search_fields = ('name', 'location', 'phone_number')

@admin.register(ShedTools)
class ShedToolsAdmin(admin.ModelAdmin):
    list_display = ('shedtool_id', 'shed', 'using_tool')
    list_filter = ('shed', 'using_tool')
    search_fields = ('shed__name', 'using_tool__instrument_name')

# @admin.register(ToolMovement)
# class ToolMovementAdmin(admin.ModelAdmin):
#     list_display = ('movement_id', 'movement_date', 'tool', 'source_shed', 'destination_shed', 'acknowledgment', 'tool_count', 'instrument_name')
#     list_filter = ('movement_date', 'source_shed', 'destination_shed', 'acknowledgment')
#     search_fields = ('movement_id', 'tool__tool_group_name', 'source_shed__name', 'destination_shed__name', 'instrument_name__instrument_name')

@admin.register(ServiceOrder)
class ServiceOrderAdmin(admin.ModelAdmin):
    list_display = ('service_id', 'date', 'amount', 'description')
    list_filter = ('date',)

@admin.register(ServiceTools)
class ServiceToolsAdmin(admin.ModelAdmin):
    list_display = ('servicetool_id', 'service', 'tool', 'vendor')  # Include 'vendor' if you added it to the model
    list_filter = ('service','vendor')

@admin.register(TransportOrder)
class TransportOrderAdmin(admin.ModelAdmin):
    list_display = ('movement_id', 'movement_date', 'source_shed', 'destination_shed', 'acknowledgment', 'tool_count')
    list_filter = ('source_shed', 'destination_shed', 'acknowledgment')
    search_fields = ('movement_id',)

@admin.register(TransportTools)
class TransportToolsAdmin(admin.ModelAdmin):
    list_display = ('transporttool_id', 'transport', 'tool')
    list_filter = ('transport',)
    search_fields = ('transport__movement_id', 'tool__instrument_name')

@admin.register(Vendor)
class VendorAdmin(admin.ModelAdmin):
    list_display = ('vendor_id', 'name', 'location', 'address', 'phone_number')
    search_fields = ('name', 'location', 'phone_number')

@admin.register(VendorHandles)
class VendorHandlesAdmin(admin.ModelAdmin):
    list_display = ('vendorhandle_id', 'vendor_name', 'tool_id', 'turnaround_time', 'cost')

    def vendor_name(self, obj):
        return obj.vendor.name

    vendor_name.short_description = 'Vendor Name'

    def tool_id(self, obj):
        return obj.tool.instrument_no

    tool_id.short_description = 'Tool ID'

@admin.register(DeliveryChallan)
class DeliveryChallanAdmin(admin.ModelAdmin):
    list_display = ('deliverychallan_id', 'received_date', 'vendor', 'shed', 'service')
    list_filter = ('vendor', 'shed', 'service')
    search_fields = ('deliverychallan_id', 'vendor__name')

@admin.register(DeliveryChallanTools)
class DeliveryChallanToolsAdmin(admin.ModelAdmin):
    list_display = ('deliverychallantool_id', 'deliverychallan', 'tool')
    list_filter = ('deliverychallan__vendor',)
    search_fields = ('deliverychallan__vendor__name',)

@admin.register(CalibrationReport)
class CalibrationAdmin(admin.ModelAdmin):
    list_display = ('calibrationtool_id', 'calibration_date', 'calibration_report_no', 'calibration_agency', 'result', 'action', 'next_calibration_date', 'remark', 'calibration_tool')
    list_filter = ('calibration_date', 'calibration_agency', 'action')
    search_fields = ('calibration_report_no', 'calibration_agency')

# @admin.register(InstrumentTransportHistory)
# class InstrumentTransportHistoryAdmin(admin.ModelAdmin):
#     list_display = ('instrument', 'movement')
#     list_filter = ('movement__source_shed', 'movement__destination_shed')
#     search_fields = ('instrument__instrument_no', 'movement__movement_id')    