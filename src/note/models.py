from django.db import models
from arnie.models import Arnia

# Create your models here.


class Nota(models.Model):
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    arnia = models.ForeignKey(Arnia, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = "Note"

    def __str__(self):
        return self.text
