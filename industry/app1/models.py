from django.db import models

class VendorType(models.Model):
    vendortype_id = models.AutoField(primary_key=True)
    vendor_type = models.CharField(max_length=32)

    def __str__(self):
        return f"{self.vendor_type}"

def default_certificate_file():
    return 'vendor_certificates/samplereport.txt'

class Vendor(models.Model):
    vendor_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=32)
    location = models.CharField(max_length=32)
    address = models.CharField(max_length=64)
    phone_number = models.CharField(max_length=12)
    email = models.EmailField()
    nabl_number = models.CharField(max_length=32, default='0', blank=True, null=True)
    nabl_certificate = models.FileField(upload_to='vendor_certificates/', default=default_certificate_file, max_length=250 , blank=True, null=True)
    vendor_type = models.ForeignKey(VendorType, on_delete=models.SET_DEFAULT, default=1)

    def __str__(self):
        return f"{self.name}"

class InstrumentGroupMaster(models.Model):
    tool_id = models.AutoField(primary_key=True)
    tool_group_name = models.CharField(max_length=32)
    tool_group_code = models.CharField(max_length=8)
    instrument_type = models.CharField(max_length=32)

    def __str__(self):
        return f"{self.tool_group_name}"

class InstrumentFamilyGroup(models.Model):
    instrumentfamilyid = models.AutoField(primary_key=True)
    instrument_family_name = models.CharField(max_length=32)
    instrument_group_master = models.ForeignKey(InstrumentGroupMaster, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.instrument_family_name}"

class InstrumentModel(models.Model):
    instrument_no = models.AutoField(primary_key=True)
    instrument_name = models.CharField(max_length=32)
    manufacturer_name = models.CharField(max_length=32, blank=True, null=True)
    year_of_purchase = models.DateField()
    gst = models.SmallIntegerField()
    description = models.CharField(max_length=160, blank=True, null=True)
    instrument_range = models.CharField(max_length=16, blank=True, null=True)
    least_count = models.CharField(max_length=8, blank=True, null=True)
    type_of_tool = models.ForeignKey(InstrumentGroupMaster, on_delete=models.DO_NOTHING)
    calibration_frequency = models.IntegerField()
    service_status = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.instrument_name} - ({self.type_of_tool})"

class ShedDetails(models.Model):
    shed_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=24)
    location = models.CharField(max_length=32)
    phone_number = models.CharField(max_length=12)

    def __str__(self):
        return f"{self.name}"

class ShedTools(models.Model):
    shedtool_id = models.AutoField(primary_key=True)
    shed = models.ForeignKey(ShedDetails, on_delete=models.CASCADE)
    using_tool = models.ForeignKey(InstrumentModel, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('using_tool',)

    def __str__(self):
        return f"{self.using_tool.instrument_name} in {self.shed.name}"

class TransportOrder(models.Model):
    movement_id = models.AutoField(primary_key=True)
    movement_date = models.DateField()
    source_shed = models.ForeignKey(ShedDetails, related_name='source_shed_transport_order', on_delete=models.CASCADE)
    destination_shed = models.ForeignKey(ShedDetails, related_name='destination_shed_transport_order', on_delete=models.CASCADE)
    acknowledgment = models.BooleanField(default=False)
    tool_count = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)    

    def __str__(self):
        return f"Tool Movement ID: {self.movement_id} - Date: {self.movement_date} -{self.source_shed} to {self.destination_shed}"

class TransportTools(models.Model):
    transporttool_id = models.AutoField(primary_key=True)
    transport = models.ForeignKey(TransportOrder, on_delete=models.CASCADE)
    tool = models.ForeignKey(InstrumentModel, on_delete=models.CASCADE)
    tool_movement_remarks = models.TextField(default="good", blank=True, null=True)
    acknowledgment = models.BooleanField(default=False)

    class Meta:
        unique_together = ('transport', 'tool')

    def __str__(self):
        return f"Transport ID: {self.transport.movement_id} - Tool: {self.tool.instrument_name}"

class ServiceType(models.Model):
    servicetype_id = models.AutoField(primary_key=True)
    service_type = models.CharField(max_length=32)

    def __str__(self):
        return f"{self.service_type}"

class ServiceOrder(models.Model):
    service_id = models.AutoField(primary_key=True)
    date = models.DateField()
    amount = models.DecimalField(max_digits=10, decimal_places=2, default=0, null=True, blank=True)  
    description = models.CharField(max_length=100)
    tool_count = models.IntegerField()
    vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
        
    def __str__(self):
        return f"Service ID: {self.service_id} - Date: {self.date} - Vendor: {self.vendor.name} - Tool Count: {self.tool_count}"

class ServiceTools(models.Model):
    servicetool_id = models.AutoField(primary_key=True)
    service = models.ForeignKey(ServiceOrder, on_delete=models.CASCADE)
    tool = models.ForeignKey(InstrumentModel, on_delete=models.CASCADE)
    vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE)
    service_type = models.ForeignKey(ServiceType, on_delete=models.SET_DEFAULT, default=1)
    service_remarks = models.TextField(default="good", blank=True, null=True)

    def __str__(self):
        return f"Service ID: {self.service.service_id} - Tool: {self.tool.instrument_name} - Service Vendor: {self.vendor.name}"

    class Meta:
        unique_together = ('service', 'tool', 'vendor')
  
class VendorHandles(models.Model):
    vendorhandle_id = models.AutoField(primary_key=True)
    vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE)
    tool = models.ForeignKey(InstrumentModel, on_delete=models.CASCADE)
    turnaround_time = models.IntegerField()
    cost = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        unique_together = ('vendor', 'tool')

    def __str__(self):
        return f"Vendor: {self.vendor.name} - Tool: {self.tool.instrument_name} - TurnAround Time: {self.turnaround_time} - Cost: {self.cost}"

class DeliveryChallan(models.Model):
    deliverychallan_id = models.AutoField(primary_key=True)
    received_date = models.DateField()
    vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE)
    shed = models.ForeignKey(ShedDetails, related_name='shed_delivery_challan', on_delete=models.CASCADE)
    service = models.ForeignKey(ServiceOrder, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"DeliveryChallan ID: {self.deliverychallan_id} - Vendor: {self.vendor.name} - Service:{self.service.service_id} -Shed: {self.shed.name}"

def default_report_file():
    return 'samplereport.txt'

class CalibrationReport(models.Model):
    calibrationtool_id = models.AutoField(primary_key=True)
    calibration_tool = models.ForeignKey(InstrumentModel, on_delete=models.CASCADE)
    calibration_date = models.DateField()
    calibration_report_no = models.CharField(max_length=32)
    calibration_agency = models.CharField(max_length=32)
    result = models.FloatField()
    action = models.CharField(max_length=16)
    next_calibration_date = models.DateField()
    notification_date = models.DateField()
    remark = models.TextField()
    calibration_report_file = models.FileField(upload_to='calibration_reports/', default=default_report_file, max_length=250 ,null=True)
    calibration_report_file2 = models.FileField(upload_to='calibration_reports2/', default=default_report_file, max_length=250 ,null=True)

    def __str__(self):
        return f"Calibration Tool: {self.calibration_tool} - Notification Date: {self.notification_date}"  

class DeliveryChallanTools(models.Model):
    deliverychallantool_id = models.AutoField(primary_key=True)
    deliverychallan = models.ForeignKey(DeliveryChallan, on_delete=models.CASCADE)
    tool = models.ForeignKey(InstrumentModel, on_delete=models.CASCADE)
    calibration_report = models.ForeignKey(CalibrationReport, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return f"DeliveryChallan ID: {self.deliverychallan.deliverychallan_id} - Tool: {self.tool.instrument_name}"

    