from django.db import models
from django.contrib.auth.models import User


class Twit(models.Model):
    nombre = models.ForeignKey("Perfil", related_name='Twit')
    creacion = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=200)


class Perfil(models.Model):
    usuario = models.OneToOneField(User)
    ciudad = models.CharField(max_length=20)
   #imagen_perfil = models.ImageField(upload_to='img')
    cumple = models.DateTimeField(auto_now_add=True)
    biografia = models.TextField(max_length=70)
    amigos = models.ManyToManyField('self', blank=True)
    permisos = models.BooleanField()
