from django.db import models

# Create your models here.
class Apicoltore(models.Model):
    name = models.CharField(max_length=30)

    class Meta:
        verbose_name_plural = "Apicolori"

    def __str__(self):
        return self.name