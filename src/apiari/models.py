from django.db import models
from django.conf import settings

# Create your models here.


class Apiario(models.Model):
    code = models.CharField(max_length=30)
    apicoltore = models.ForeignKey(settings.AUTH_USER_MODEL,
                                   on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = "Apiari"

    def __str__(self):
        return self.code
