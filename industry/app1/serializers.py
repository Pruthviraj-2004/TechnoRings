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

class ShedDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShedDetails
        fields = '__all__'

class ShedToolsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShedTools
        fields = '__all__'

class ServiceOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = ServiceOrder
        fields = '__all__'

class ServiceToolsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ServiceTools
        fields = '__all__'

class TransportToolsSerializer(serializers.ModelSerializer):
    class Meta:
        model = TransportTools
        fields = '__all__'

class TransportOrderSerializer(serializers.ModelSerializer):
    tools = TransportToolsSerializer(many=True, read_only=True)  # Assuming 'tools' is the related name for TransportTools in TransportOrder model

    class Meta:
        model = TransportOrder
        fields = '__all__'

class VendorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vendor
        fields = '__all__'

class VendorHandlesSerializer(serializers.ModelSerializer):
    class Meta:
        model = VendorHandles
        fields = '__all__'

class DeliveryChallanSerializer(serializers.ModelSerializer):
    class Meta:
        model = VendorHandles
        fields = '__all__'

class CalibrationReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = VendorHandles
        fields = '__all__'

class DeliveryChallanToolsSerializer(serializers.ModelSerializer):
    class Meta:
        model = VendorHandles
        fields = '__all__'        