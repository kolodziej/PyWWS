from django.db import models
from pywws.settings import LANGUAGES

class Tag(models.Model):
	name = models.CharField(max_length=32)
	slug = models.SlugField(max_length=32)

	def __str__(self):
		return self.name

class Category(models.Model):
	name = models.CharField(max_length=55)
	slug = models.SlugField(max_length=55)
	lang = models.CharField(max_length=5, choices=LANGUAGES)

	def __str__(self):
		return self.name

class Article(models.Model):
	title = models.CharField(max_length=255)
	slug = models.SlugField(max_length=120)
	intro = models.TextField()
	content = models.TextField()
	pub_date = models.DateTimeField()
	mod_date = models.DateTimeField(auto_now=True)
	lang = models.CharField(max_length=5, choices=LANGUAGES)
	published = models.BooleanField(default=False)
	deleted = models.BooleanField(default=False)
	category = models.ForeignKey("Category")
	tags = models.ManyToManyField("Tag", blank=True)
	related_articles = models.ManyToManyField("self", blank=True)
	related_notes = models.ManyToManyField("Note", blank=True)

	def __str__(self):
		return self.title


class Note(models.Model):
	title = models.CharField(max_length=255)
	slug = models.SlugField(max_length=120)
	content = models.TextField()
	pub_date = models.DateTimeField()
	mod_date = models.DateTimeField()
	lang = models.CharField(max_length=5, choices=LANGUAGES)
	published = models.BooleanField(default=False)
	deleted = models.BooleanField(default=False)
	category = models.ForeignKey("Category")
	tags = models.ManyToManyField("Tag", blank=True)
	related_notes = models.ManyToManyField("self", blank=True)
	related_articles = models.ManyToManyField("Article", blank=True)

	def __str__(self):
		return self.title
