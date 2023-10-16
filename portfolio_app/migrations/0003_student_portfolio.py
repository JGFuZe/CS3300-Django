# Generated by Django 4.2.5 on 2023-10-10 00:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("portfolio_app", "0002_portfolio_project_alter_student_major"),
    ]

    operations = [
        migrations.AddField(
            model_name="student",
            name="portfolio",
            field=models.OneToOneField(
                default=2,
                on_delete=django.db.models.deletion.CASCADE,
                to="portfolio_app.portfolio",
            ),
            preserve_default=False,
        ),
    ]