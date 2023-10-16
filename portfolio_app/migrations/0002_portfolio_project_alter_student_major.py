# Generated by Django 4.2.5 on 2023-10-09 23:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("portfolio_app", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Portfolio",
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
                ("title", models.CharField(max_length=200)),
                ("contact_email", models.CharField(max_length=200)),
                ("is_active", models.BooleanField(default=False)),
                ("about", models.TextField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name="Project",
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
                ("title", models.CharField(max_length=200)),
                ("discription", models.TextField()),
            ],
        ),
        migrations.AlterField(
            model_name="student",
            name="major",
            field=models.CharField(
                choices=[
                    ("CSCI-BS", "BS in Computer Science"),
                    ("CPEN-BS", "BS in Computer Engineering"),
                    ("BIGD-BI", "BI in Game Design and Development"),
                    ("BICS-BI", "BI in Computer Science"),
                    ("BISC-BI", "BI in Computer Security"),
                    ("CSCI-BA", "BA in Computer Science"),
                    ("DASE-BS", "BS in Data Analytics and Systems Engineering"),
                ],
                max_length=200,
            ),
        ),
    ]