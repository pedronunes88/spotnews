# Generated by Django 4.2.3 on 2024-05-13 16:11

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("news", "0003_news"),
    ]

    operations = [
        migrations.CreateModel(
            name="Author",
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
                ("name", models.CharField(max_length=100)),
            ],
        ),
    ]
