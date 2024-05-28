# Generated by Django 4.2.11 on 2024-05-25 12:51

import app1.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("app1", "0031_alter_calibrationreport_calibration_report_file"),
    ]

    operations = [
        migrations.AddField(
            model_name="vendor",
            name="email",
            field=models.EmailField(default="abc@gmail.com", max_length=254),
        ),
        migrations.AddField(
            model_name="vendor",
            name="nabl_certificate",
            field=models.FileField(
                blank=True,
                default=app1.models.default_certificate_file,
                max_length=250,
                null=True,
                upload_to="vendor_certificates/",
            ),
        ),
        migrations.AddField(
            model_name="vendor",
            name="nabl_number",
            field=models.CharField(
                blank=True, default="1717171717", max_length=32, null=True
            ),
        ),
        migrations.AlterField(
            model_name="vendor",
            name="phone_number",
            field=models.CharField(max_length=12),
        ),
    ]