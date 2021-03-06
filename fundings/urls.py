from django.urls import path
from . import views


app_name = "fundings"

urlpatterns = [
    path("create/", views.CreateFundingView.as_view(), name="create"),
    path("<int:pk>/", views.FundingDetail.as_view(), name="detail"),
    path("<int:pk>/edit/", views.EditFundingView.as_view(), name="edit"),
    path("<int:pk>/photos/", views.FundingPhotosView.as_view(), name="photos"),
    path("<int:pk>/photos/add/", views.AddPhotoView.as_view(), name="add-photo"),
    path(
        "<int:funding_pk>/photos/<int:photo_pk>/delete/",
        views.delete_photo,
        name="delete-photo",
    ),
    path(
        "<int:funding_pk>/photos/<int:photo_pk>/edit/",
        views.EditPhotoView.as_view(),
        name="edit-photo",
    ),
    path("search/", views.SearchView.as_view(), name="search"),
]
