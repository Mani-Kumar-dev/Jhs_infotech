# Generated by Django 4.1.1 on 2023-02-22 09:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("app1", "0008_rename_person_select_registration_select_course"),
    ]

    operations = [
        migrations.CreateModel(
            name="Registration_2",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("reservation_name_2", models.CharField(max_length=55)),
                ("reservation_email_2", models.EmailField(max_length=254)),
                ("reservation_phone_2", models.BigIntegerField()),
                ("select_course_2", models.CharField(max_length=55)),
                ("Date_2", models.DateField()),
                ("form_message_2", models.TextField(blank=True, default="", null=True)),
            ],
        ),
    ]