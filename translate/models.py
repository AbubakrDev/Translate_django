from django.db import models
from django.urls import reverse

class TranslatePage(models.Model):
    name = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    

    def __str__(self):
        return self.name
