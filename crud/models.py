from django.db import models


# Create your models here.

class FileStorage(models.Model):
    file = models.FileField()
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Person(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    age = models.PositiveIntegerField()
    department = models.CharField(max_length=50)
    is_active = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class ClassRoom(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class PersonProfile(models.Model):
    person = models.OneToOneField(Person, on_delete=models.CASCADE, related_name="person_profile")
    profile_picture = models.FileField(upload_to="profile_picture")
    bio = models.TextField(max_length=500)
    address = models.CharField(max_length=20)
    classroom = models.ForeignKey(ClassRoom, on_delete=models.CASCADE, related_name="classroom_people")

    # def __str__(self):
    #     return self.name