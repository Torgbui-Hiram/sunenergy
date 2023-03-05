from django.db import models
from django.utils import timezone

# Create your models here.


class Quotation(models.Model):
    name = models.CharField(max_length=50, blank=True, null=True)
    email = models.EmailField()
    phone = models.CharField(max_length=20, blank=True, null=True)
    requirement = models.CharField(max_length=2080)
    quote_date = models.DateTimeField(auto_now_add=timezone.now)

    def __str__(self):
        return str(self.name)
