# Generated by Django 4.1.1 on 2023-02-22 10:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("app1", "0010_rename_reservation_name_2_registration_2_name_2"),
    ]

    operations = [
        migrations.DeleteModel(name="Registration_2",),
    ]
