# Generated by Django 4.2.5 on 2023-10-10 00:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("portfolio_app", "0007_alter_project_portfolio_projectsinportfolio"),
    ]

    operations = [
        migrations.RemoveField(model_name="projectsinportfolio", name="portfolio",),
        migrations.RemoveField(model_name="projectsinportfolio", name="project",),
        migrations.DeleteModel(name="Project",),
        migrations.DeleteModel(name="ProjectsInPortfolio",),
    ]