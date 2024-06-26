# Generated by Django 4.2.13 on 2024-06-19 20:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("app1", "0005_alter_shedtools_using_tool"),
    ]

    operations = [
        migrations.AlterField(
            model_name="shedtools",
            name="shed",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.PROTECT, to="app1.sheddetails"
            ),
        ),
        migrations.AlterField(
            model_name="shedtools",
            name="using_tool",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="app1.instrumentmodel"
            ),
        ),
    ]