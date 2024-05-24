from rest_framework import serializers
from .models import *

class InstrumentGroupMasterSerializer(serializers.ModelSerializer):
    class Meta:
        model = InstrumentGroupMaster
        fields = '__all__'

class InstrumentFamilyGroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = InstrumentFamilyGroup
        fields = '__all__'

class InstrumentModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = InstrumentModel
        fields = '__all__'

class ShedToolsSerializer(serializers.ModelSerializer):
    using_tool = InstrumentModelSerializer()

    class Meta:
        model = ShedTools
        fields = '__all__'

class ShedDetailsSerializer(serializers.ModelSerializer):
    shed_tools = ShedToolsSerializer(many=True, read_only=True)

    class Meta:
        model = ShedDetails
        fields = '__all__'

class ServiceToolsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ServiceTools
        fields = '__all__'
        
class ServiceOrderSerializer(serializers.ModelSerializer):
    tools = ServiceToolsSerializer(many=True, read_only=True)
    class Meta:
        model = ServiceOrder
        fields = '__all__'

class TransportToolsSerializer(serializers.ModelSerializer):
    class Meta:
        model = TransportTools
        fields = '__all__'

class TransportOrderSerializer(serializers.ModelSerializer):
    tools = TransportToolsSerializer(many=True, read_only=True)

    class Meta:
        model = TransportOrder
        fields = '__all__'

class VendorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vendor
        fields = '__all__'

class VendorHandlesSerializer(serializers.ModelSerializer):
    tool_name = serializers.CharField(source='tool.instrument_name', read_only=True)

    class Meta:
        model = VendorHandles
        fields = ['vendorhandle_id', 'turnaround_time', 'cost', 'vendor', 'tool', 'tool_name']


class DeliveryChallanSerializer(serializers.ModelSerializer):
    class Meta:
        model = DeliveryChallan
        fields = '__all__'

class CalibrationReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = CalibrationReport
        fields = '__all__'

class DeliveryChallanToolsSerializer(serializers.ModelSerializer):
    class Meta:
        model = DeliveryChallanTools
        fields = '__all__'  
          