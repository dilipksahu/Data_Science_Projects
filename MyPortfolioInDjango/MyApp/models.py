from django.db import models

# Create your models here.
class MySkill(models.Model):
    skill = models.CharField(max_length=100)
    percent = models.IntegerField()


class Service(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()

