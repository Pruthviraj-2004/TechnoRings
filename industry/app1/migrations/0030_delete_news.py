# Generated by Django 4.2.11 on 2024-04-23 09:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("app1", "0029_calibrationreport_calibration_report_file"),
    ]

    operations = [
        migrations.DeleteModel(name="News",),
    ]