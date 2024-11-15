from django.db import models


# Create your models here.


class Groups(models.Model):
    GAME_VERSIONS = (
        ("D&D", "D&D"),
        ("M&M", "Mutants & Masterminds"),
        ("PF", "Pathfinder"),
        ("Other", "Other"),
    )

    group_pic = models.ImageField(default="app/static/test.png")
    group_name = models.CharField(max_length=100)
    group_description = models.TextField()
    members = models.JSONField()
    game_version = models.CharField(
        max_length=100,
        choices=GAME_VERSIONS,
    )
