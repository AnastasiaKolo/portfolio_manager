from django.contrib import admin
from .models import Tag, Category, Artwork, Project, Event, Artist


# Register your models here.
admin.site.register(Tag)
admin.site.register(Category)
admin.site.register(Artwork)
admin.site.register(Project)
admin.site.register(Event)
admin.site.register(Artist)
