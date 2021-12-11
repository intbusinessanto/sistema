from django.db import models

# Create your models here.
class Libro(models.Model):
    id= models.AutoField(primary_key=True)
    titulo = models.CharField(max_length=100, verbose_name='Titulo')
    imagen = models.ImageField(upload_to='imagenes/', verbose_name="Imagen", mull=True)
    descripcion = models.TextField( verbose_name="Descripción", null=True)