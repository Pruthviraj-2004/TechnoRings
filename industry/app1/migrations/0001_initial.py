# Generated by Django 4.2.13 on 2024-06-23 05:37

import app1.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="CalibrationReport",
            fields=[
                (
                    "calibrationtool_id",
                    models.AutoField(primary_key=True, serialize=False),
                ),
                ("calibration_date", models.DateField()),
                ("calibration_report_no", models.CharField(max_length=32)),
                (
                    "calibration_agency",
                    models.CharField(
                        blank=True, default=None, max_length=32, null=True
                    ),
                ),
                (
                    "result",
                    models.CharField(
                        blank=True, default=None, max_length=16, null=True
                    ),
                ),
                (
                    "action",
                    models.CharField(
                        blank=True, default=None, max_length=16, null=True
                    ),
                ),
                ("next_calibration_date", models.DateField()),
                ("notification_date", models.DateField()),
                (
                    "remark",
                    models.TextField(blank=True, default="Calibration", null=True),
                ),
                (
                    "calibration_report_file",
                    models.FileField(
                        default=app1.models.default_report_file,
                        max_length=250,
                        null=True,
                        upload_to="calibration_reports/",
                    ),
                ),
                (
                    "calibration_report_file2",
                    models.FileField(
                        default=app1.models.default_report_file,
                        max_length=250,
                        null=True,
                        upload_to="calibration_reports2/",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="DeliveryChallan",
            fields=[
                (
                    "deliverychallan_id",
                    models.AutoField(primary_key=True, serialize=False),
                ),
                ("received_date", models.DateField()),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name="InstrumentFamilyGroup",
            fields=[
                (
                    "instrument_family_id",
                    models.AutoField(primary_key=True, serialize=False),
                ),
                ("instrument_family_name", models.CharField(max_length=32)),
            ],
        ),
        migrations.CreateModel(
            name="InstrumentGroupMaster",
            fields=[
                ("tool_group_id", models.AutoField(primary_key=True, serialize=False)),
                ("tool_group_name", models.CharField(max_length=32)),
                ("tool_group_code", models.CharField(max_length=8)),
                (
                    "tool_family",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="app1.instrumentfamilygroup",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="ServiceType",
            fields=[
                ("servicetype_id", models.AutoField(primary_key=True, serialize=False)),
                ("service_type", models.CharField(max_length=32)),
            ],
        ),
        migrations.CreateModel(
            name="ShedDetails",
            fields=[
                ("shed_id", models.AutoField(primary_key=True, serialize=False)),
                ("name", models.CharField(max_length=24)),
                ("location", models.CharField(max_length=32)),
                ("phone_number", models.CharField(max_length=12)),
                ("password", models.CharField(default="1234", max_length=16)),
                (
                    "shed_note",
                    models.TextField(blank=True, default="Everything clear", null=True),
                ),
            ],
        ),
        migrations.CreateModel(
            name="TransportOrder",
            fields=[
                ("movement_id", models.AutoField(primary_key=True, serialize=False)),
                ("movement_date", models.DateField()),
                ("acknowledgment", models.BooleanField(default=False)),
                ("tool_count", models.IntegerField()),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                (
                    "destination_shed",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="destination_shed_transport_order",
                        to="app1.sheddetails",
                    ),
                ),
                (
                    "source_shed",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="source_shed_transport_order",
                        to="app1.sheddetails",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="VendorType",
            fields=[
                ("vendortype_id", models.AutoField(primary_key=True, serialize=False)),
                ("vendor_type", models.CharField(max_length=32)),
            ],
        ),
        migrations.CreateModel(
            name="Vendor",
            fields=[
                ("vendor_id", models.AutoField(primary_key=True, serialize=False)),
                ("name", models.CharField(max_length=32)),
                ("location", models.CharField(max_length=32)),
                ("address", models.CharField(max_length=64)),
                ("phone_number", models.CharField(max_length=12)),
                ("email", models.EmailField(max_length=254)),
                (
                    "nabl_number",
                    models.CharField(blank=True, default="0", max_length=32, null=True),
                ),
                (
                    "nabl_certificate",
                    models.FileField(
                        blank=True,
                        default=app1.models.default_certificate_file,
                        max_length=250,
                        null=True,
                        upload_to="vendor_certificates/",
                    ),
                ),
                (
                    "vendor_type",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="app1.vendortype",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="ShedUser",
            fields=[
                ("sheduser_id", models.AutoField(primary_key=True, serialize=False)),
                (
                    "user",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="app1.sheddetails",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="ServiceOrder",
            fields=[
                ("service_id", models.AutoField(primary_key=True, serialize=False)),
                ("date", models.DateField()),
                (
                    "amount",
                    models.DecimalField(
                        blank=True,
                        decimal_places=2,
                        default=0,
                        max_digits=10,
                        null=True,
                    ),
                ),
                (
                    "description",
                    models.TextField(blank=True, default="Service", null=True),
                ),
                ("tool_count", models.IntegerField()),
                ("service_pending", models.BooleanField(default=True)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                (
                    "vendor",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="app1.vendor",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="InstrumentModel",
            fields=[
                ("instrument_no", models.AutoField(primary_key=True, serialize=False)),
                ("instrument_name", models.CharField(max_length=32)),
                (
                    "manufacturer_name",
                    models.CharField(
                        blank=True, default=None, max_length=32, null=True
                    ),
                ),
                ("year_of_purchase", models.DateField(blank=True, null=True)),
                ("gst", models.SmallIntegerField(blank=True, default=18, null=True)),
                (
                    "description",
                    models.CharField(
                        blank=True, default=None, max_length=160, null=True
                    ),
                ),
                (
                    "instrument_range",
                    models.CharField(
                        blank=True, default=None, max_length=16, null=True
                    ),
                ),
                (
                    "least_count",
                    models.CharField(blank=True, default=None, max_length=8, null=True),
                ),
                (
                    "calibration_frequency",
                    models.IntegerField(blank=True, default=365, null=True),
                ),
                ("service_status", models.BooleanField(default=False)),
                (
                    "current_shed",
                    models.ForeignKey(
                        blank=True,
                        default=6,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="app1.sheddetails",
                    ),
                ),
                (
                    "type_of_tool",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="app1.instrumentgroupmaster",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="DeliveryChallanTools",
            fields=[
                (
                    "deliverychallantool_id",
                    models.AutoField(primary_key=True, serialize=False),
                ),
                (
                    "calibration_report",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="app1.calibrationreport",
                    ),
                ),
                (
                    "deliverychallan",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="app1.deliverychallan",
                    ),
                ),
                (
                    "tool",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="app1.instrumentmodel",
                    ),
                ),
            ],
        ),
        migrations.AddField(
            model_name="deliverychallan",
            name="service",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="app1.serviceorder"
            ),
        ),
        migrations.AddField(
            model_name="deliverychallan",
            name="shed",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="shed_delivery_challan",
                to="app1.sheddetails",
            ),
        ),
        migrations.AddField(
            model_name="deliverychallan",
            name="vendor",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to="app1.vendor",
            ),
        ),
        migrations.AddField(
            model_name="calibrationreport",
            name="calibration_tool",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="app1.instrumentmodel"
            ),
        ),
        migrations.CreateModel(
            name="VendorHandles",
            fields=[
                (
                    "vendorhandle_id",
                    models.AutoField(primary_key=True, serialize=False),
                ),
                ("turnaround_time", models.IntegerField()),
                ("cost", models.DecimalField(decimal_places=2, max_digits=10)),
                (
                    "tool",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="app1.instrumentmodel",
                    ),
                ),
                (
                    "vendor",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="app1.vendor"
                    ),
                ),
            ],
            options={"unique_together": {("vendor", "tool")},},
        ),
        migrations.CreateModel(
            name="TransportTools",
            fields=[
                (
                    "transporttool_id",
                    models.AutoField(primary_key=True, serialize=False),
                ),
                (
                    "tool_movement_remarks",
                    models.TextField(blank=True, default="Transport Tool", null=True),
                ),
                ("acknowledgment", models.BooleanField(default=False)),
                (
                    "tool",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="app1.instrumentmodel",
                    ),
                ),
                (
                    "transport",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="app1.transportorder",
                    ),
                ),
            ],
            options={"unique_together": {("transport", "tool")},},
        ),
        migrations.CreateModel(
            name="ShedTools",
            fields=[
                ("shedtool_id", models.AutoField(primary_key=True, serialize=False)),
                (
                    "shed",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="app1.sheddetails",
                    ),
                ),
                (
                    "using_tool",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="app1.instrumentmodel",
                    ),
                ),
            ],
            options={"unique_together": {("using_tool",)},},
        ),
        migrations.CreateModel(
            name="ServiceTools",
            fields=[
                ("servicetool_id", models.AutoField(primary_key=True, serialize=False)),
                (
                    "service_remarks",
                    models.TextField(blank=True, default="Service Tool", null=True),
                ),
                ("service_pending_tool", models.BooleanField(default=True)),
                (
                    "service",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="app1.serviceorder",
                    ),
                ),
                (
                    "service_type",
                    models.ForeignKey(
                        default=1,
                        on_delete=django.db.models.deletion.SET_DEFAULT,
                        to="app1.servicetype",
                    ),
                ),
                (
                    "tool",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="app1.instrumentmodel",
                    ),
                ),
                (
                    "vendor",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="app1.vendor",
                    ),
                ),
            ],
            options={"unique_together": {("service", "tool", "vendor")},},
        ),
    ]
