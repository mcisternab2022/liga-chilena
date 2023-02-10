from django.db import models
from cloudinary.models import CloudinaryField

# Create your models here.
class Equipo(models.Model):
  nombre_equipo = models.CharField(max_length=50)
  imagen = CloudinaryField('escudos')

  def __str__(self):
      return self.nombre_equipo


class Jugador(models.Model):
  nombre_jugador = models.CharField(max_length=200)
  equipo = models.ForeignKey(Equipo, on_delete=models.PROTECT)
  foto = CloudinaryField('jugadores')
  fecha_nacimiento = models.DateField()
  dorsal = models.IntegerField()
  goles = models.IntegerField()
  asistencias = models.IntegerField()
  amarillas = models.IntegerField()
  rojas = models.IntegerField()

  def __str__(self):
      return self.nombre_jugador

class Tabla(models.Model):
  equipo = models.ForeignKey(Equipo, on_delete=models.CASCADE)
  puntos = models.IntegerField()
  goles_favor = models.IntegerField()
  goles_contra = models.IntegerField()
  partidos_ganados = models.IntegerField()
  partidos_perdidos = models.IntegerField()
  partidos_empatados = models.IntegerField()
  partidos_jugados = models.IntegerField()
  diferencia = models.IntegerField()

  def __str__(self):
      return "%s" % (self.equipo)