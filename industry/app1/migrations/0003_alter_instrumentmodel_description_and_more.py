# Generated by Django 4.2.11 on 2024-03-16 05:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("app1", "0002_alter_instrumentgroupmaster_instrument_type"),
    ]

    operations = [
        migrations.AlterField(
            model_name="instrumentmodel",
            name="description",
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name="instrumentmodel",
            name="instrument_range",
            field=models.CharField(blank=True, max_length=12, null=True),
        ),
        migrations.AlterField(
            model_name="instrumentmodel",
            name="least_count",
            field=models.CharField(blank=True, max_length=8, null=True),
        ),
        migrations.AlterField(
            model_name="instrumentmodel",
            name="manufacturer_name",
            field=models.CharField(blank=True, max_length=24, null=True),
        ),
    ]