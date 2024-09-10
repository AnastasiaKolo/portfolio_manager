""" Forms for Catalog app """
from django.forms import ModelForm, CharField, FileInput, ImageField

from .models import Artwork, Tag, Event, Project, Artist


class TagForm(ModelForm):
    """ Tag creation form """
    tag_text = CharField(max_length=100)

    class Meta:
        model = Tag
        fields = ["tag_text",]


class ArtistForm(ModelForm):
    """ Artist register form """
    image = ImageField(widget=FileInput(attrs={'class': 'form-control-file'}))

    class Meta:
        model = Artist
        fields = [
            "alias",
            "user",
            "bio",
            "cv",
            "statement",
            "image"
        ]


class ArtworkForm(ModelForm):
    """ Artwork upload form """
    image = ImageField(widget=FileInput(attrs={'class': 'form-control-file'}))

    class Meta:
        model = Artwork
        fields = [
            "title",
            "author",
            "category",
            "description",
            "materials",
            "created",
            "length",
            "width",
            "height",
            "availability",
            "price",
            "tags",
            "image"
        ]


class EventForm(ModelForm):
    """ Event creation form """
    poster = ImageField(widget=FileInput(attrs={'class': 'form-control-file'}))

    class Meta:
        model = Event
        fields = [
            "name",
            "type",
            "description",
            "contact",
            "place",
            "link",
            "date",
            "deadline",
            "comment",
            # artworks, 
            "poster"
        ]


class ProjectForm(ModelForm):
    """ Project creation form """
    image = ImageField(widget=FileInput(attrs={'class': 'form-control-file'}))

    class Meta:
        model = Project
        fields = [
            "title",
            "author",
            "description",
            "created",
            # "artworks",
            "image"
        ]
