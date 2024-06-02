from rest_framework import serializers
from .models import InstrumentFamilyGroup, InstrumentGroupMaster, CalibrationReport, DeliveryChallan, DeliveryChallanTools, InstrumentModel,  ServiceOrder, ServiceTools, ServiceType, ShedTools, TransportOrder, ShedDetails, TransportTools, Vendor, VendorHandles, VendorType

class InstrumentGroupMasterSerializer(serializers.ModelSerializer):
    class Meta:
        model = InstrumentGroupMaster
        fields = '__all__'

class InstrumentFamilyGroupSerializer(serializers.ModelSerializer):
    instrument_group_master_name = serializers.CharField(source='instrument_group_master.tool_group_name', read_only=True)

    class Meta:
        model = InstrumentFamilyGroup
        fields = ['instrumentfamilyid', 'instrument_family_name', 'instrument_group_master', 'instrument_group_master_name']

class InstrumentModelSerializer(serializers.ModelSerializer):
    type_of_tool_name = serializers.CharField(source='type_of_tool.tool_group_name', read_only=True)

    class Meta:
        model = InstrumentModel
        fields = [
            'instrument_no', 'instrument_name', 'manufacturer_name', 'year_of_purchase', 'gst', 
            'description', 'instrument_range', 'least_count', 'calibration_frequency', 
            'service_status', 'type_of_tool', 'type_of_tool_name'
        ]

class SimpleInstrumentModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = InstrumentModel
        fields = ['instrument_no', 'instrument_name']

class ShedToolsSerializer(serializers.ModelSerializer):
    using_tool = SimpleInstrumentModelSerializer()
    shed_name = serializers.CharField(source='shed.name', read_only=True)

    class Meta:
        model = ShedTools
        fields = ['shedtool_id', 'using_tool', 'shed', 'shed_name']

class ShedDetailsSerializer(serializers.ModelSerializer):
    shed_tools = ShedToolsSerializer(many=True, read_only=True)

    class Meta:
        model = ShedDetails
        fields = '__all__'

class TransportToolsSerializer(serializers.ModelSerializer):
    tool_name = serializers.CharField(source='tool.instrument_name', read_only=True)

    class Meta:
        model = TransportTools
        fields = ['transporttool_id', 'tool_movement_remarks', 'acknowledgment', 'transport', 'tool', 'tool_name']

class TransportOrderSerializer(serializers.ModelSerializer):
    source_shed_name = serializers.CharField(source='source_shed.name', read_only=True)
    destination_shed_name = serializers.CharField(source='destination_shed.name', read_only=True)
    tools = TransportToolsSerializer(many=True, read_only=True)

    class Meta:
        model = TransportOrder
        fields = ['movement_id', 'movement_date', 'acknowledgment', 'tool_count', 'created_at', 'updated_at',
                  'source_shed', 'source_shed_name', 'destination_shed', 'destination_shed_name', 'tools']

class ServiceTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ServiceType
        fields = '__all__'

class ServiceToolsSerializer(serializers.ModelSerializer):
    vendor_name = serializers.CharField(source='vendor.name', read_only=True)
    service_type_name = serializers.CharField(source='service_type.service_type', read_only=True)
    tool_name = serializers.CharField(source='tool.instrument_name', read_only=True)

    class Meta:
        model = ServiceTools
        fields = ['servicetool_id', 'service_remarks', 'service', 'tool', 'tool_name', 'vendor', 'vendor_name', 'service_type', 'service_type_name']
        
class ServiceOrderSerializer(serializers.ModelSerializer):
    tools = ServiceToolsSerializer(many=True, read_only=True)
    vendor_name = serializers.CharField(source='vendor.name', read_only=True)

    class Meta:
        model = ServiceOrder
        fields = ['service_id', 'date', 'amount', 'description', 'tool_count', 'created_at', 'updated_at', 'vendor', 'vendor_name', 'tools']

class VendorTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = VendorType
        fields = '__all__'

class VendorSerializer(serializers.ModelSerializer):
    vendor_type_name = serializers.CharField(source='vendor_type.vendor_type', read_only=True)

    class Meta:
        model = Vendor
        fields = [
            'vendor_id', 'name', 'location', 'address', 'phone_number', 'email', 
            'nabl_number', 'nabl_certificate', 'vendor_type', 'vendor_type_name'
        ]

class VendorHandlesSerializer(serializers.ModelSerializer):
    tool_name = serializers.CharField(source='tool.instrument_name', read_only=True)
    vendor_name = serializers.CharField(source='vendor.name', read_only=True)

    class Meta:
        model = VendorHandles
        fields = ['vendorhandle_id', 'turnaround_time', 'cost', 'vendor', 'vendor_name', 'tool', 'tool_name']

class DeliveryChallanSerializer(serializers.ModelSerializer):
    vendor_name = serializers.CharField(source='vendor.name', read_only=True)
    shed_name = serializers.CharField(source='shed.name', read_only=True)
    
    class Meta:
        model = DeliveryChallan
        fields = ['deliverychallan_id', 'received_date', 'vendor', 'vendor_name', 'shed', 'shed_name', 'service', 'created_at', 'updated_at']

class CalibrationReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = CalibrationReport
        fields = '__all__'

class DeliveryChallanToolsSerializer(serializers.ModelSerializer):
    tool_name = serializers.CharField(source='tool.instrument_name', read_only=True)
    
    class Meta:
        model = DeliveryChallanTools
        fields = ['deliverychallantool_id', 'deliverychallan', 'tool', 'tool_name', 'calibration_report']
          