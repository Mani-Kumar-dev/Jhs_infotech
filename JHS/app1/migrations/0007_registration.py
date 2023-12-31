# Generated by Django 4.1.1 on 2023-02-22 07:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("app1", "0006_alter_gallery_img"),
    ]

    operations = [
        migrations.CreateModel(
            name="Registration",
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
                ("reservation_name", models.CharField(max_length=55)),
                ("reservation_email", models.EmailField(max_length=254)),
                ("reservation_phone", models.BigIntegerField()),
                ("person_select", models.CharField(max_length=55)),
                ("Date", models.DateField()),
                ("form_message", models.TextField(blank=True, default="", null=True)),
            ],
        ),
    ]
