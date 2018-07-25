from django.db import models


# Create your models here.

class IcoList(models.Model):
    name = models.CharField(max_length=50)
    ico_scale = models.IntegerField()
    total = models.IntegerField()

    def __str__(self):
        return self.name
