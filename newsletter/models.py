from django.db import models

class Subscriber(models.Model):
	name = models.CharField(max_length=60)
	email = models.EmailField(unique=True)
	checksum = models.CharField(max_length=64, unique=True)
	activated = models.BooleanField(default=False)

	def __str__(self):
		return self.name + " <" + self.email + ">"
