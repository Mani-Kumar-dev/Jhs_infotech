# Generated by Django 4.1.1 on 2023-02-23 17:39

from django.db import migrations, models
import embed_video.fields


class Migration(migrations.Migration):

    dependencies = [
        ("app1", "0011_delete_registration_2"),
    ]

    operations = [
        migrations.CreateModel(
            name="Placements",
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
                ("video_url", embed_video.fields.EmbedVideoField()),
            ],
        ),
    ]