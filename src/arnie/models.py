from django.db import models
from apiari.models import Apiario

# Create your models here.


class Arnia(models.Model):
    code = models.CharField(max_length=30)
    apiario = models.ForeignKey(Apiario, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = "Arnie"

    def __str__(self):
        return self.code
