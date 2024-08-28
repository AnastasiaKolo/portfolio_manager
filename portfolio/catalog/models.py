""" Models for Portfolio application """
import datetime 
from typing import Union

from django.contrib import admin
from django.contrib.auth.models import User
from django.db import models, transaction
from django.utils import timezone

from django.urls import reverse


class Tag(models.Model):
    """ Tags for works/projects """
    text = models.CharField(max_length=200, unique=True, help_text="Enter tags for an item")

    def __str__(self):
        return f"{self.text}"

    class Meta:
        constraints = [
            models.UniqueConstraint(
                models.functions.Lower('text'),
                name='text_case_insensitive_unique',
                violation_error_message = "Tag already exists (case insensitive match)"
            ),
        ]
        ordering = ["text"]


    def get_absolute_url(self):
        """Returns the URL to access a particular instance of the model."""
        return reverse('catalog:tag_detail', args=[str(self.text)])


class Category(models.Model):
    """ An artwork category: Painting, Print, Photography, Sculpture """
    name = models.CharField(max_length=200, help_text="Enter category name")
    description = models.CharField(max_length=2000, help_text="Enter category description")

    class Meta:
        constraints = [
            models.UniqueConstraint(
                models.functions.Lower('name'),
                name='name_case_insensitive_unique',
                violation_error_message = "Category already exists (case insensitive match)"
            ),
        ]
        ordering = ["name"]

    def __str__(self):
        return f"{self.name}"


class Artwork(models.Model):
    """ A single piece of art """
    title = models.CharField(max_length=200, help_text="Enter title for an item")
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.PROTECT)
    description = models.CharField(max_length=2000, help_text="Enter item description")
    materials = models.CharField(max_length=200, help_text="Enter materials for an item")
    created = models.DateTimeField("date created", default=timezone.now)
    length = models.IntegerField()
    width = models.IntegerField()
    height = models.IntegerField()
    availability = models.BooleanField(default=False)
    price = models.IntegerField()
    tags = models.ManyToManyField(Tag, related_name="artworks", help_text="Select tags for this artwork")

    def __str__(self):
            return f"{self.title}, {self.created}"

    def get_absolute_url(self):
        """Returns the URL to access a particular instance of the model."""
        return reverse('catalog:artwork_detail', args=[str(self.id)])

    @property
    def url(self):
        return self.get_absolute_url()

    def display_tags(self):
        """Create a string for the Tags. This is required to display tags in Admin."""
        return ', '.join(tag.tag_text for tag in self.tags.all())

    display_tags.short_description = 'Tags'


class Project(models.Model):
    """ A project can unite several artworks """
    title = models.CharField(max_length=200, help_text="Enter title for an item")
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.CharField(max_length=2000, help_text="Enter item description")
    created = models.DateTimeField("date created", default=timezone.now)
    artworks = models.ManyToManyField(Artwork, related_name="projects",
        help_text="Select artworks for this project ")

