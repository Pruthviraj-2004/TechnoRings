# Generated by Django 4.2.13 on 2024-06-15 19:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("app1", "0046_alter_calibrationreport_remark_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="calibrationreport",
            name="result",
            field=models.CharField(max_length=16),
        ),
    ]