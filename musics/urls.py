from django.urls import path
from . import views

app_name = "musics"

urlpatterns = [
    path("<int:pk>/", views.MusicDetail.as_view(), name="mdetail"),
    path("<int:pk>/edit/", views.EditMusicView.as_view(), name="edit"),
    path("<int:pk>/photos/", views.MusicPhotosView.as_view(), name="photos"),
    path(
        "<int:music_pk>/photos/<int:photo_pk>/delete/",
        views.delete_photo,
        name="delete-photo",
    ),
    path(
        "<int:music_pk>/photos/<int:photo_pk>/edit/",
        views.EditPhotoView.as_view(),
        name="edit-photo",
    ),
]
