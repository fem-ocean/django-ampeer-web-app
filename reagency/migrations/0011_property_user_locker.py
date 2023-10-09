# Generated by Django 4.2.3 on 2023-10-02 15:13

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("reagency", "0010_alter_property_landlord"),
    ]

    operations = [
        migrations.AddField(
            model_name="property",
            name="user_locker",
            field=models.ForeignKey(
                blank=True,
                default="",
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="paiduser",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
    ]
