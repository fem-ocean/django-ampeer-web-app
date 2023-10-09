# Generated by Django 4.2.3 on 2023-08-30 13:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("reagency", "0003_location_street2_alter_location_estate_name"),
    ]

    operations = [
        migrations.AddField(
            model_name="scoutedproperty",
            name="reason_for_rejection",
            field=models.TextField(default=""),
        ),
        migrations.AddField(
            model_name="scoutedproperty",
            name="status",
            field=models.CharField(default="pending", max_length=50),
        ),
    ]
