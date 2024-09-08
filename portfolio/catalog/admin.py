from django.contrib import admin
from .models import Tag, Category, Artwork, Project, Event


# Register your models here.
admin.site.register(Tag)
admin.site.register(Category)
admin.site.register(Artwork)
admin.site.register(Project)
admin.site.register(Event)
