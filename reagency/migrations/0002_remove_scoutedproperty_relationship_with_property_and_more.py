# Generated by Django 4.2.3 on 2023-08-29 06:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("reagency", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="scoutedproperty",
            name="relationship_with_property",
        ),
        migrations.AddField(
            model_name="location",
            name="estate_name2",
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name="location",
            name="estate_name",
            field=models.CharField(blank=True, default="", max_length=250, null=True),
        ),
    ]
