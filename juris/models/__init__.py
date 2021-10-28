from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.urls import reverse
# Create your models here.


class Actualizacion(models.Model):
    titulo = models.CharField(max_length=30, default="Expediente actualizado")
    contenido = models.CharField(max_length=200)
    fecha_actualizacion = models.DateField(auto_now=True)
    expediente = models.ForeignKey('Expediente',
                                   on_delete=models.SET_NULL,
                                   null=True)

    def get_rol(self):
        return str(self.expediente.intervenientes.rol)

    def get_absolute_url(self):
        """Devuelve el url para acceder cada actualizacion"""
        return reverse('actualizacion-detail-view', args=[str(self.id)])

    def __str__(self):
        return " " + self.titulo + " exp: "


# Modelo expediente que guarda todos los datos pertinentes al caso
class Expediente(models.Model):
    numero_de_fiscalia = models.CharField(max_length=5)
    letra = models.CharField(max_length=1)
    año = models.DateField(auto_now=True)
    tribunal = models.CharField(max_length=2)
    numero_expediente = models.CharField(max_length=6)
    intervenientes = models.ManyToManyField(User,
                                            through='PersonasIntervenientes')

    # Los campos especificados en unique_together son para que no hayan dos expedientes iguales
    class Meta:
        unique_together = ('numero_de_fiscalia', 'letra', 'tribunal',
                           'numero_expediente')

    def get_year(self):
        return str(self.año.year)

    def return_list_of_intervenientes(self):
        return self.intervenientes.through.objects.filter(expediente=self)

    def return_list(self):
        return '_'.join(
            [str(inter.rol) for inter in self.intervenientes.all()])

    def __str__(self):
        return str(
            self.id
        ) + " " + self.numero_de_fiscalia + "-" + self.letra + "-" + str(
            self.año.year) + "-" + self.tribunal + "-" + self.numero_expediente


# Modelo para gobernar la relacion Many-To-Many que relaciona el expediente
# con la persona
# Hacerlo de esta forma permite establecer una relacion de
# Un expediente puede estar asociado a muchas personas
# y un usuario puede estar asociado a multiples expedientes
class PersonasIntervenientes(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    expediente = models.ForeignKey(Expediente, on_delete=models.CASCADE)
    fecha_incluido = models.DateField(auto_now=True)
    ROL_USUARIO = (('DE', 'DEMANDADO'), ('DD', 'DEMANDANTE'), ('FF', 'FISCAL'),
                   ('JZ', 'JUEZ'), ('AD', 'ABOGADO DEFENSOR'),
                   ('SE', 'SECRETARIO DEFENSOR'), ('TE', 'TESTIGO'),
                   ('PE', 'PERSONA EXTRA'))
    rol = models.CharField(max_length=2,
                           choices=ROL_USUARIO,
                           help_text="Rol del usuario en el caso",
                           default='PE')

    #Los campos en unique_together son para que en un mismo expediente no se puede agregar un mismo usuario con un mismo rol
    #mas de una vez
    class Meta:
        unique_together = ('user', 'rol', 'expediente')

    def __str__(self):
        return self.rol + " " + self.user.username
