from django import forms
from .models import CalibrationReport, DeliveryChallan, DeliveryChallanTools, InstrumentFamilyGroup, InstrumentGroupMaster, InstrumentModel, ServiceOrder, ServiceTools, ShedTools, TransportOrder, ShedDetails, TransportTools, Vendor, VendorHandles

class InstrumentForm(forms.ModelForm):
    class Meta:
        model = InstrumentModel
        fields = ['instrument_name', 'manufacturer_name', 'year_of_purchase', 'gst', 'description', 'instrument_range', 'least_count', 'type_of_tool', 'calibration_frequency']

class InstrumentGroupMasterForm(forms.ModelForm):
    class Meta:
        model = InstrumentGroupMaster
        fields = ['tool_group_name', 'tool_group_code', 'instrument_type']

class InstrumentFamilyGroupForm(forms.ModelForm):
    class Meta:
        model = InstrumentFamilyGroup
        fields = ['instrument_family_name', 'instrument_group_master']

class TransportMovementOrderForm(forms.ModelForm):
    class Meta:
        model = TransportOrder
        fields = ['movement_date', 'source_shed', 'destination_shed', 'tool_count']

    def __init__(self, *args, **kwargs):
        super(TransportMovementOrderForm, self).__init__(*args, **kwargs)
        self.fields['source_shed'].queryset = ShedDetails.objects.all()
        self.fields['destination_shed'].queryset = ShedDetails.objects.all()

class TransportToolsForm(forms.ModelForm):
    class Meta:
        model = TransportTools
        fields = ['transport', 'tool']

class ServiceToolsForm(forms.ModelForm):
    class Meta:
        model = ServiceTools
        fields = ['service', 'tool']

class ServiceOrderForm(forms.Form):
    date = forms.DateField()
    amount = forms.DecimalField(max_digits=10, decimal_places=2)
    description = forms.CharField(max_length=100)
    tool_count = forms.IntegerField()

class TransportOrderForm(forms.ModelForm):
    class Meta:
        model = TransportOrder
        fields = ['movement_date', 'source_shed', 'destination_shed', 'tool_count']

class TransportToolsForm(forms.ModelForm):
    class Meta:
        model = TransportTools
        fields = ['tool']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['tool'].queryset = InstrumentModel.objects.all()

class AnotherServiceOrderForm(forms.ModelForm):
    class Meta:
        model = ServiceOrder
        fields = ['date', 'amount', 'description', 'tool_count', 'vendor']

class AnotherServiceToolForm(forms.ModelForm):
    class Meta:
        model = ServiceTools
        fields = ['tool']

class DeliveryChallanForm(forms.ModelForm):
    class Meta:
        model = DeliveryChallan
        fields = ['received_date', 'vendor', 'shed', 'service']

class DeliveryChallanToolsForm(forms.ModelForm):
    class Meta:
        model = DeliveryChallanTools
        fields = ['tool']

class CalibrationReportForm(forms.ModelForm):
    class Meta:
        model = CalibrationReport
        # fields = ['calibration_date', 'calibration_report_no', 'calibration_agency', 'result', 'action', 'next_calibration_date', 'notification_date','remark']
        fields = ['calibration_date', 'calibration_report_no', 'calibration_agency', 'result', 'action', 'remark']

DeliveryChallanToolsFormSet = forms.inlineformset_factory(DeliveryChallan, DeliveryChallanTools, form=DeliveryChallanToolsForm, extra=1)

class InstrumentFamilyGroupForm1(forms.ModelForm):
    class Meta:
        model = InstrumentFamilyGroup
        fields = ['instrument_family_name']

class InstrumentGroupMasterForm1(forms.ModelForm):
    instrument_group_name = forms.CharField(max_length=24)
    instrument_group_code = forms.CharField(max_length=8)
    instrument_type = forms.CharField(max_length=12)
    class Meta:
        model = InstrumentGroupMaster
        fields = []

class InstrumentModelForm1(forms.ModelForm):
    class Meta:
        model = InstrumentModel
        exclude = ['type_of_tool']

class ShedDetailsForm(forms.ModelForm):
    class Meta:
        model = ShedDetails
        fields = '__all__'

class ShedToolsForm(forms.ModelForm):
    class Meta:
        model = ShedTools
        fields = '__all__'
        
class VendorForm(forms.ModelForm):
    class Meta:
        model = Vendor
        fields = '__all__'

class VendorHandlesForm(forms.ModelForm):
    class Meta:
        model = VendorHandles
        fields = '__all__'
