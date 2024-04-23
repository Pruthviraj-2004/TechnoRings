# Generated by Django 4.2.11 on 2024-04-23 09:22

import app1.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("app1", "0028_news"),
    ]

    operations = [
        migrations.AddField(
            model_name="calibrationreport",
            name="calibration_report_file",
            field=models.FileField(
                default=app1.models.default_report_file,
                upload_to="calibration_reports/",
            ),
        ),
    ]
