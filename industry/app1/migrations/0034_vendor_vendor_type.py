# Generated by Django 4.2.11 on 2024-05-26 13:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("app1", "0033_vendortype"),
    ]

    operations = [
        migrations.AddField(
            model_name="vendor",
            name="vendor_type",
            field=models.ForeignKey(
                default=2,
                on_delete=django.db.models.deletion.SET_DEFAULT,
                to="app1.vendortype",
            ),
        ),
    ]