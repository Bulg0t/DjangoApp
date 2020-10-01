from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Klasa(models.Model):
    nazwa = models.CharField("nazwa Klasy", max_length=4, default="")
    rok_matury = models.IntegerField("rok Matury", default=0)
    rok_naboru = models.IntegerField("rok Naboru", default=0)
class Absolwent(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    klasa = models.ForeignKey(Klasa, on_delete=models.SET_NULL, blank=True, null=True)

