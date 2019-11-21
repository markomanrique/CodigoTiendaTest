from django.db import models

# Create your models here.

class Categoria (models.Model):
    descripcion = models.TextField(null=True,blank=True)
    
    def __str__(self):
        return self.descripcion
        
class Producto (models.Model):
    descripcion = models.TextField(null=True,blank=True)
    categoria = models.ForeignKey(Categoria,on_delete=models.CASCADE,related_name="productosname")

    def __str__(self):
        return self.descripcion
