from django.db import models

class Vendor(models.Model):
    vendor_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=24)
    location = models.CharField(max_length=16)
    address = models.CharField(max_length=64)
    phone_number = models.CharField(max_length=10)

    def __str__(self):
        return f"Vendor Name: {self.name}"

class InstrumentGroupMaster(models.Model):
    tool_id = models.AutoField(primary_key=True)
    tool_group_name = models.CharField(max_length=24)
    tool_group_code = models.CharField(max_length=8)
    instrument_type = models.CharField(max_length=16)

    def __str__(self):
        return f"{self.tool_group_name}"

class InstrumentFamilyGroup(models.Model):
    instrumentfamilyid = models.AutoField(primary_key=True)
    instrument_family_name = models.CharField(max_length=24)
    instrument_group_master = models.ForeignKey(InstrumentGroupMaster, on_delete=models.CASCADE)

    def __str__(self):
        return f"Instrument Family Name: {self.instrument_family_name}"

class InstrumentModel(models.Model):
    instrument_no = models.AutoField(primary_key=True)
    instrument_name = models.CharField(max_length=16)
    manufacturer_name = models.CharField(max_length=24, blank=True, null=True)
    year_of_purchase = models.DateField()
    gst = models.SmallIntegerField()
    description = models.CharField(max_length=255, blank=True, null=True)
    instrument_range = models.CharField(max_length=16, blank=True, null=True)
    least_count = models.CharField(max_length=8, blank=True, null=True)
    type_of_tool = models.ForeignKey(InstrumentGroupMaster, on_delete=models.DO_NOTHING)
    calibration_frequency = models.IntegerField()

    def __str__(self):
        return f"{self.instrument_name} ({self.type_of_tool})"

class ShedDetails(models.Model):
    shed_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=24)
    location = models.CharField(max_length=16)
    phone_number = models.CharField(max_length=10)

    def __str__(self):
        return self.name

class ShedTools(models.Model):
    shedtool_id = models.AutoField(primary_key=True)
    shed = models.ForeignKey(ShedDetails, on_delete=models.DO_NOTHING)
    using_tool = models.ForeignKey(InstrumentModel, on_delete=models.DO_NOTHING)

    def __str__(self):
        return f"{self.using_tool.instrument_name} in {self.shed.name}"
  
class ToolMovement(models.Model):
    movement_id = models.AutoField(primary_key=True)
    movement_date = models.DateField()
    tool = models.ForeignKey(InstrumentGroupMaster, on_delete=models.DO_NOTHING) 
    source_shed = models.ForeignKey(ShedDetails, related_name='tool_movement_source_shed', on_delete=models.DO_NOTHING)
    destination_shed = models.ForeignKey(ShedDetails, related_name='tool_movement_destination', on_delete=models.DO_NOTHING)
    acknowledgment = models.BooleanField(default=False)
    tool_count = models.IntegerField()
    instrument_name = models.ForeignKey(InstrumentModel, on_delete=models.DO_NOTHING)

    def __str__(self):
        return f"Movement ID: {self.movement_id} - Date: {self.movement_date}"

class ServiceOrder(models.Model):
    service_id = models.AutoField(primary_key=True)
    date = models.DateField()
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.CharField(max_length=100)
    tool_count = models.IntegerField()
    vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE)

    def __str__(self):
        return f"Service ID: {self.service_id}"

class ServiceTools(models.Model):
    servicetool_id = models.AutoField(primary_key=True)
    service = models.ForeignKey(ServiceOrder, on_delete=models.DO_NOTHING)
    tool = models.ForeignKey(InstrumentModel, on_delete=models.DO_NOTHING)
    vendor = models.ForeignKey(Vendor, on_delete=models.DO_NOTHING)  # Add this field

    def __str__(self):
        return f"Service ID: {self.service.service_id} - Tool ID: {self.tool.instrument_no} - Service Vendor: {self.vendor}"

    class Meta:
        unique_together = ('service', 'tool', 'vendor')

class TransportOrder(models.Model):
    movement_id = models.AutoField(primary_key=True)
    movement_date = models.DateField()
    source_shed = models.ForeignKey(ShedDetails, related_name='source_shed_transport_order', on_delete=models.DO_NOTHING)
    destination_shed = models.ForeignKey(ShedDetails, related_name='destination_shed_transport_order', on_delete=models.DO_NOTHING)
    acknowledgment = models.BooleanField(default=False)
    tool_count = models.IntegerField()

    def __str__(self):
        return f"Movement ID: {self.movement_id} - Date: {self.movement_date}"

class TransportTools(models.Model):
    transporttool_id = models.AutoField(primary_key=True)
    transport = models.ForeignKey(TransportOrder, on_delete=models.CASCADE)
    tool = models.ForeignKey(InstrumentModel, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('transport', 'tool')

    def __str__(self):
        return f"TransportTool ID: {self.transporttool_id} - Transport ID: {self.transport.movement_id} - Tool ID: {self.tool.instrument_no}"
   
class VendorHandles(models.Model):
    vendorhandle_id = models.AutoField(primary_key=True)
    vendor = models.ForeignKey(Vendor, on_delete=models.DO_NOTHING)
    tool = models.ForeignKey(InstrumentModel, on_delete=models.DO_NOTHING)
    turnaround_time = models.IntegerField()
    cost = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"Vendor: {self.vendor.name} - Tool: {self.tool.instrument_no} - TurnAround Time: {self.turnaround_time}"

class DeliveryChallan(models.Model):
    deliverychallan_id = models.AutoField(primary_key=True)
    received_date = models.DateField()
    vendor = models.ForeignKey(Vendor, on_delete=models.DO_NOTHING)
    shed = models.ForeignKey(ShedDetails, related_name='shed_delivery_challan', on_delete=models.DO_NOTHING)
    service = models.ForeignKey(ServiceOrder, on_delete=models.DO_NOTHING)

    def __str__(self):
        return f"DeliveryChallan ID: {self.deliverychallan_id} - Vendor: {self.vendor.name}"

class DeliveryChallanTools(models.Model):
    deliverychallantool_id = models.AutoField(primary_key=True)
    deliverychallan = models.ForeignKey(DeliveryChallan, on_delete=models.DO_NOTHING)
    tool = models.ForeignKey(InstrumentModel, on_delete=models.DO_NOTHING)

    def __str__(self):
        return f"DeliveryChallan ID: {self.deliverychallan.deliverychallan_id} - Tool ID: {self.tool.instrument_no}"

    