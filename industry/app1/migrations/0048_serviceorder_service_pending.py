# Generated by Django 4.2.13 on 2024-06-15 19:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("app1", "0047_alter_calibrationreport_result"),
    ]

    operations = [
        migrations.AddField(
            model_name="serviceorder",
            name="service_pending",
            field=models.BooleanField(default=False),
        ),
    ]