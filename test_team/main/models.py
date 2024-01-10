from django.db import models


class Person(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Team(models.Model):
    name = models.CharField(max_length=100)
    members = models.ManyToManyField(Person, related_name='teams', blank=True)

    def __str__(self):
        return self.name
