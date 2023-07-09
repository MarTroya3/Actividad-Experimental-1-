from django.db import models

# Create your models here.
class Entidadinventario(models.Model):
    nombre = models.CharField(max_length=30)
    siglas = models.CharField(max_length=30)
    numero_tienda = models.IntegerField()
    ciudad = models.CharField(max_length=100)

    def __str__(self):
        return """Nombre: %s - Siglas: %s \n
                Numeronegocio: %d\n
                Ciudad: %s""" % (self.nombre,
                self.siglas,
                self.numero_tienda,
                self.ciudad)

class Entidadproducto(models.Model):
    nombre = models.CharField(max_length=30)
    siglas = models.CharField(max_length=30)
    numero_producto = models.IntegerField()
    detalle = models.CharField(max_length=100)

    def __str__(self):
        return """Nombre: %s - Siglas: %s \n
                Numeroproducto: %d\n
                Detalle: %s""" % (self.nombre,
                self.siglas,
                self.numero_producto,
                self.detalle)