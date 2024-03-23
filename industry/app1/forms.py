from django import forms
from .models import DeliveryChallan, DeliveryChallanTools, InstrumentModel, ServiceOrder, ServiceTools, TransportOrder, ShedDetails, TransportTools

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
DeliveryChallanToolsFormSet = forms.inlineformset_factory(
    DeliveryChallan, 
    DeliveryChallanTools, 
    form=DeliveryChallanToolsForm,
    extra=1  # Number of extra forms to display
)    