from django.urls import path
from . import views

app_name = "musics"

urlpatterns = [
    path("<int:pk>/", views.MusicDetail.as_view(), name="mdetail"),
]
