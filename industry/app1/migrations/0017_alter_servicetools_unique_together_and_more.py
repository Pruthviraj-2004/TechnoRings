# Generated by Django 4.2.11 on 2024-03-21 12:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("app1", "0016_serviceorder_vendor"),
    ]

    operations = [
        migrations.AlterUniqueTogether(name="servicetools", unique_together=set(),),
        migrations.AddField(
            model_name="servicetools",
            name="vendor",
            field=models.ForeignKey(
                default=1,
                on_delete=django.db.models.deletion.DO_NOTHING,
                to="app1.vendor",
            ),
            preserve_default=False,
        ),
        migrations.AlterUniqueTogether(
            name="servicetools", unique_together={("service", "tool", "vendor")},
        ),
    ]
