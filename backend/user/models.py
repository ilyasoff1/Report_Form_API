from django.db import models
from django.contrib.auth.models import AbstractUser


class Profile(AbstractUser):
    contact = models.IntegerField(null=True, blank=True)
    department = models.CharField(max_length=50, null=True, blank=True)

    def __str__(self):
        return self.username

    def save(self, *args, **kwargs):
        self.set_password(self.password) 
        super().save(*args, **kwargs)

