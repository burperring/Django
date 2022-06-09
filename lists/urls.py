from django.urls import path
from . import views


app_name = "lists"

urlpatterns = [
    path("toggle/<int:music_pk>", views.toggle_music, name="toggle-music"),
    path("favs/", views.SeeFavsView.as_view(), name="see-favs"),
]
