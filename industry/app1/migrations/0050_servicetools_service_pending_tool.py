# Generated by Django 4.2.13 on 2024-06-15 19:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("app1", "0049_alter_instrumentmodel_unique_together"),
    ]

    operations = [
        migrations.AddField(
            model_name="servicetools",
            name="service_pending_tool",
            field=models.BooleanField(default=False),
        ),
    ]