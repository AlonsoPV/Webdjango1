from django.db import models

# Create your models here.
class Project(models.Model):
    title = models.CharField(max_length=200, verbose_name='Título') #campo de caracteres
    description = models.TextField(verbose_name='Descripción')
    image = models.ImageField(verbose_name='Imagen', upload_to="projects")
    created = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')
    updated = models.DateTimeField(auto_now=True, verbose_name='Fecha de edición')

    class Meta:
        verbose_name ="proyecto"
        verbose_name_plural = "proyectos"
        ordering = ["-created"] #de mas reciente a mas antiguo
#Se puede crear un vista donde haya formulario// Interaccion con la pagina
    def __str__(self):
        return self.title