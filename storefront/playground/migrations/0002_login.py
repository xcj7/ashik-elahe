# Generated by Django 4.2.5 on 2023-09-30 09:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("playground", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Login",
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
                ("name", models.CharField(max_length=255)),
                ("password", models.TextField()),
            ],
        ),
    ]