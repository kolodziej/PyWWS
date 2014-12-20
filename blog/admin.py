from django.contrib import admin
from blog.models import Tag, Category, Article, Note

admin.site.register(Article)
admin.site.register(Note)
admin.site.register(Tag)
admin.site.register(Category)
