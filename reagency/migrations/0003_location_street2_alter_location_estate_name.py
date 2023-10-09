# Generated by Django 4.2.3 on 2023-08-29 12:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("reagency", "0002_remove_scoutedproperty_relationship_with_property_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="location",
            name="street2",
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name="location",
            name="estate_name",
            field=models.CharField(default="", max_length=250),
        ),
    ]