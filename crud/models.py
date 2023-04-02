from django.db import models


# Create your models here.
class Person(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    age = models.PositiveIntegerField()
    department = models.CharField(max_length=50)
    is_active = models.BooleanField(default=False)

    def __str__(self):
        return self.name
