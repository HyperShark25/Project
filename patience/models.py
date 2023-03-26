from django.db import models
from django.contrib.auth.models import User


class Blog(models.Model):
    pin_number = models.PositiveIntegerField(primary_key=True)
    title = models.CharField(max_length=25)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    email = models.EmailField()
    description = models.TextField(null=True)

    def __str__(self):
        return self.title
