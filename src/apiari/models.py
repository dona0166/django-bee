from django.db import models
from apicoltori.models import Apicoltore

# Create your models here.


class Apiario(models.Model):
    code = models.CharField(max_length=30)
    apicolore = models.ForeignKey(Apicoltore, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = "Apiari"

    def __str__(self):
        return self.code
