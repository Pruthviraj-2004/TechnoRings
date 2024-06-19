# Generated by Django 4.2.13 on 2024-06-19 20:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("app1", "0004_alter_instrumentmodel_unique_together_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="shedtools",
            name="using_tool",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.DO_NOTHING,
                to="app1.instrumentmodel",
            ),
        ),
    ]
