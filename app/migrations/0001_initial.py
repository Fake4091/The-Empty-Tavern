# Generated by Django 4.2.16 on 2024-11-12 17:00

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Player",
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
                (
                    "gamever",
                    models.CharField(
                        choices=[
                            ("D&D", "D&D"),
                            ("PF", "Pathfinder"),
                            ("M&M", "Mutants&Masterminds"),
                            ("Other", "Other"),
                        ],
                        default="D&D",
                        max_length=21,
                    ),
                ),
                (
                    "user",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]
