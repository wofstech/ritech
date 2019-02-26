from django.db import models

class Letter(models.Model):
    subEmail = models.EmailField()
