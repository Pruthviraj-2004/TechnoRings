# Generated by Django 4.2.13 on 2024-06-01 20:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("app1", "0040_transporttools_acknowledgment"),
    ]

    operations = [
        migrations.AlterField(
            model_name="serviceorder",
            name="amount",
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
        ),
    ]
