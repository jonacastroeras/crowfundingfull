from django.db import models


# Create your models here.
class Project(models.Model):
    name = models.CharField(max_length=80, verbose_name="Nombre")
    image = models.ImageField(verbose_name="Imagen", upload_to="proyectos", blank=False, null=True)
    description = models.TextField(max_length=500, verbose_name="Descripción")
    amount = models.FloatField(verbose_name="Monto")

    class Meta:
        verbose_name = "Proyecto"
        verbose_name_plural = "Proyectos"

    def __str__(self):
        return self.name


class Donation(models.Model):
    amount = models.FloatField(verbose_name="Monto")
    donant = models.CharField(max_length=200, verbose_name="Donante")
    is_anonymus = models.BooleanField(verbose_name="Anónimo")
    project = models.ForeignKey(Project, on_delete=models.CASCADE, verbose_name="Proyecto")

    class Meta:
        verbose_name = "Donación"
        verbose_name_plural = "Donaciones"

    def __str__(self):
        return self.donant
