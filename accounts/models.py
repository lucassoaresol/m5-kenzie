from django.db import models
from django.contrib.auth.models import AbstractUser


class Account(AbstractUser):
    name = models.CharField(max_length=255)
    age = models.IntegerField()
    sex = models.CharField(max_length=255)

    def __str__(self) -> str:
        return f"Account object ({self.id})"
