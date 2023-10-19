# Generated by Django 4.2.5 on 2023-10-19 04:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("portfolio_app", "0012_delete_projectsinportfolio"),
    ]

    operations = [
        migrations.CreateModel(
            name="ThemeChanger",
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
                ("is_dark", models.BooleanField(default=False)),
            ],
        ),
    ]