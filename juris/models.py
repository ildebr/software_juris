from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.urls import reverse
# Create your models here.


# Modelo de perfil que extiende del modelo usuario
# Aqui se especifica el rol que desempeña el usuario en el caso
class Profile(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	
	# @receiver(post_save, sender=User)
	# def create_user_profile(sender, instance, created, **kwargs):
	# 	if created:
	# 		Profile.objects.create(user=instance)

	# @receiver(post_save, sender=User)
	# def  save_user_profile(sender, instance, **kwargs):
	# 	user = instance
	# 	instance.profile.save()

	@receiver(post_save, sender=User)
	def save_profile(sender, instance,created, **kwargs):
		user = instance
		if created:
			profile = Profile(user=user)
			profile.save()

	def __str__(self):
		return self.user.username



# Modelo expediente que guarda todos los datos pertinentes al caso
class Expediente(models.Model):
	numero_de_fiscalia = models.CharField(max_length=5)
	letra = models.CharField(max_length=1)
	año = models.DateField(auto_now=True)
	tribunal = models.CharField(max_length=2)
	numero_expediente = models.CharField(max_length=6)
	intervenientes = models.ManyToManyField(Profile, through='PersonasIntervenientes')

	def get_absolute_url(self):
		return reverse('expediente-detail', args=[str(self.id)])

	# Los campos especificados en unique_together son para que no hayan dos expedientes iguales
	class Meta:
		unique_together= ('numero_de_fiscalia', 'letra', 'tribunal', 'numero_expediente')

	def __str__(self):
		return "pk" + " " + str(self.id) + " " + self.numero_de_fiscalia + "-" + self.letra + "-" + str(self.año.year) + "-" + self.tribunal + "-" + self.numero_expediente

# Modelo para gobernar la relacion Many-To-Many que relaciona el expediente
# con la persona
# Hacerlo de esta forma permite establecer una relacion de
# Un expediente puede estar asociado a muchas personas
# y un usuario puede estar asociado a multiples expedientes
class PersonasIntervenientes(models.Model):
	persona = models.ForeignKey(Profile, on_delete=models.CASCADE)
	expediente = models.ForeignKey(Expediente, on_delete=models.CASCADE)
	fecha_incluido = models.DateField(auto_now=True)
	ROL_USUARIO = (
		('DE','DEMANDADO'),
		('DD', 'DEMANDANTE'),
		('FF', 'FISCAL'),
		('JZ', 'JUEZ'),
		('AD', 'ABOGADO DEFENSOR'),
		('SE', 'SECRETARIO DEFENSOR'),
		('TE', 'TESTIGO'),
		('PE', 'PERSONA EXTRA')
	)
	rol = models.CharField(
		max_length=2,
		choices=ROL_USUARIO,
		help_text="Rol del usuario en el caso",
		default='PE')

	#Los campos en unique_together son para que en un mismo expediente no se puede agregar un mismo usuario con un mismo rol 
	#mas de una vez
	class Meta:
		unique_together = ('persona', 'rol', 'expediente')

	def __str__(self):
		return self.expediente.numero_de_fiscalia + " " + self.persona.user.username + " " + self.rol


class Actualizacion(models.Model):
	expediente = models.ForeignKey(Expediente, on_delete=models.CASCADE)
	titulo = models.CharField(max_length=30, default="Expediente actualizado")
	contenido = models.CharField(max_length=200)
	fecha_actualizacion = models.DateField(auto_now=True)

	def __str__(self):
		return self.expediente.numero_de_fiscalia + " " + self.titulo + " exp: " + str(self.expediente.id)