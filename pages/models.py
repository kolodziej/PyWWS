from django.db import models
from pywws.settings import LANGUAGES

class Page(models.Model):
	title = models.CharField(max_length=55)
	slug = models.SlugField(max_length=55)
	content = models.TextField()
	mod_date = models.DateField()
	lang = models.CharField(max_length=5, choices=LANGUAGES)
	published = models.BooleanField(default=False)
	deleted = models.BooleanField(default=False)
	related_pages = models.ManyToManyField("self", blank=True)

	def __str__(self):
		return self.title
