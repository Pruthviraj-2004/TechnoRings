# Generated by Django 4.2.13 on 2024-06-19 05:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("app1", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(model_name="sheddetails", name="user",),
    ]
