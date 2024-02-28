from django.db import models

# Create your models here.

class ApiModel(models.Model):
    url = models.URLField(
        max_length=100,
        blank=False,
        null=True,
    )