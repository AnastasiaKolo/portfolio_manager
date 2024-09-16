""" URLs for catalog app """
from django.urls import path
from . import views

app_name = 'catalog'

urlpatterns = [
    # ex: /catalog/
    path("", views.ArtworkListView.as_view(), name="index"),
    path("search/", views.ArtworkSearchListView.as_view(), name="search_results"),
    # ex: /catalog/artwork/5/ - artwork_detail view
    path("artwork/<int:pk>/", views.ArtworkDetailView.as_view(), name="artwork_detail"),
    # ex: /catalog/artwork/upload/ - upload new artwork
    path("artwork/upload/", views.ArtworkUpload.as_view(), name='artwork_upload'),
    # ex: /catalog/artist/create/ - upload new artwork
    path("artist/create/", views.ArtistCreate.as_view(), name='artist_create'),
    # ex: /catalog/artist/5/ - artist detail view
    path("artist/<int:pk>/", views.ArtistDetailView.as_view(), name="artist_detail"),
    # ex: /catalog/artist/list/ - list all tags
    path("artist/list/", views.ArtistListView.as_view(), name='artist_list'),
    # ex: /catalog/tag/create/ - create new tag
    path("tag/create/", views.TagCreate.as_view(), name='tag_create'),
    # ex: /catalog/tag/list/ - list all tags
    path("tag/list/", views.TagListView.as_view(), name='tag_list'),
    # ex: /catalog/tag/tag_text - display all artworks with this tag
    path("tag/<str:tag_text>/", views.ArtworkByTagListView.as_view(), name="tag_detail"),
    # ex: /catalog/project/create/ - create new project
    path("project/create/", views.ProjectCreate.as_view(), name='project_create'),
    # ex: /catalog/project/list/ - list all projects
    path("project/list/", views.ProjectListView.as_view(), name='project_list'),
    # ex: /catalog/project/5/ - project detail view
    path("project/<int:pk>/", views.ProjectDetailView.as_view(), name="project_detail"),
    # ex: /catalog/event/create/ - create new event
    path("event/create/", views.EventCreate.as_view(), name='event_create'),
    # ex: /catalog/event/list/ - list all events
    path("event/list/", views.EventListView.as_view(), name='event_list'),
    # ex: /catalog/event/5/ - event detail view
    path("event/<int:pk>/", views.EventDetailView.as_view(), name="event_detail"),

]
