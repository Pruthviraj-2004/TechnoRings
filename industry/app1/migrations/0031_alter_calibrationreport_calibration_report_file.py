# Generated by Django 4.2.11 on 2024-04-23 10:28

import app1.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("app1", "0030_delete_news"),
    ]

    operations = [
        migrations.AlterField(
            model_name="calibrationreport",
            name="calibration_report_file",
            field=models.FileField(
                default=app1.models.default_report_file,
                max_length=250,
                null=True,
                upload_to="calibration_reports/",
            ),
        ),
    ]
