# Generated by Django 4.2.5 on 2023-10-16 22:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("portfolio_app", "0009_project_projectsinportfolio"),
    ]

    operations = [
        migrations.DeleteModel(name="ProjectsInPortfolio",),
    ]
