from django.db import models

# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=26)
    surname = models.CharField(max_length=26)
    year = models.CharField(max_length=4)
    address = models.CharField(max_length=52)

    def __str__(self):
        return f"{self.name} {self.surname}"