# Generated by Django 4.1.1 on 2023-02-22 09:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("app1", "0009_registration_2"),
    ]

    operations = [
        migrations.RenameField(
            model_name="registration_2",
            old_name="reservation_name_2",
            new_name="name_2",
        ),
    ]