from django.db import models

targets = (
	('_blank', 'Nowa karta'),
	('_parent', 'Okno nadrzędne'),
)

class Link(models.Model):
	link = models.URLField()
	text = models.CharField(max_length=100)
	description = models.CharField(max_length=300, blank=True)
	target = models.CharField(max_length=10, choices=targets)

	def __str__(self):
		return self.text + " (" + self.link + ")"

	def get_link(self):
		return '<a href="' + self.link + '" target="' + self.target + '">' + self.text + '</a>'
	__str__.allow_tags = True

class Menu(models.Model):
	name = models.CharField(max_length=32)
	links = models.ManyToManyField("Link", blank=True)

	def __str__(self):
		return self.name
