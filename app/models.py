from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Player(models.Model):
    user = models.OneToOneField(
        User, default=User.objects.all()[0], on_delete=models.CASCADE, primary_key=True
    )
    gamever = models.CharField(
        max_length=21,
        choices=(
            ("D&D", "D&D"),
            ("PF", "Pathfinder"),
            ("M&M", "Mutants&Masterminds"),
            ("Other", "Other"),
        ),
        default="D&D",
    )
