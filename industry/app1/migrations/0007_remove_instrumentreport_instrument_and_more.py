# Generated by Django 4.2.11 on 2024-03-16 13:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("app1", "0006_alter_toolmovement_destination_shed_and_more"),
    ]

    operations = [
        migrations.RemoveField(model_name="instrumentreport", name="instrument",),
        migrations.DeleteModel(name="AcceptancePendingList",),
        migrations.DeleteModel(name="InstrumentReport",),
    ]
