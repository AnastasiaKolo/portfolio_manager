""" Views for catalog app """

from django.conf import settings
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core import paginator
from django.core.mail import send_mail

from django.db.models import Q, Count
from django.db.models.query import QuerySet
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseBadRequest, HttpRequest

from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse, resolve, reverse_lazy
from django.utils.text import Truncator
from django.views.generic import ListView, DetailView, RedirectView
from django.views.generic.edit import CreateView

from .models import Artwork, Category, Tag, Project, Event
from .forms import ArtworkForm, TagForm, EventForm, ProjectForm


class BaseArtworkListView(ListView):
    """ View for artworks list (search results, tags, etc.)"""
    template_name = "catalog/artwork_list.html"
    context_object_name = "artworks"
    allow_empty = True
    model = Artwork
    paginate_by = settings.PAGINATE_ARTWORKS
    queryset: QuerySet


class ArtworkListView(BaseArtworkListView):
    """ View for listing all artworks """
    def get_queryset(self):
        """ Return ordered artworks list """
        artworks = self.model.objects.prefetch_related("tags").order_by("-created")
        return artworks


class ArtworkSearchListView(BaseArtworkListView):
    
    def get_queryset(self):
        """ Return ordered artworks list as query results """
        query = self.request.GET.get("query")

        if query is None:
            artworks_for_query = self.model.objects.all()

        artworks_for_query = self.model.objects.filter(
            Q(title__icontains=query) | Q(description__icontains=query)
        )

        return artworks_for_query.order_by("-created")


class ArtworkByTagListView(BaseArtworkListView):

    def get_queryset(self):
        """ Return artworks by given tag """
        tag_text = self.kwargs.get("tag_text")
        tag = get_object_or_404(Tag, text=tag_text)
        artworks_by_tag = tag.artworks.all()

        return artworks_by_tag

class TagListView(ListView):
    """ List all tags """
    model = Tag
    paginate_by = 100


class ArtworkDetailView(DetailView):
    """ Shows Artwork details"""
    model = Artwork
    template_name = "catalog/artwork_detail.html"
    context_object_name = "artwork"


class TagCreate(LoginRequiredMixin, CreateView):
    """ Create new tag """
    model = Tag
    form_class = TagForm
    success_url = reverse_lazy("catalog:tag_list")


class ArtworkUpload(LoginRequiredMixin, CreateView):
    """ Upload Artwork """
    model = Artwork
    form_class = ArtworkForm

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
