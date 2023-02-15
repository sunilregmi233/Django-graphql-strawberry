from django.contrib import admin
from .models import Author, Tag, Article
# Register your models here.
admin.site.register(Author)
admin.site.register(Tag)
admin.site.register(Article)