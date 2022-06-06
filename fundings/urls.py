from django.urls import path
from . import views


app_name = "fundings"

urlpatterns = [
    path("<int:pk>/", views.FundingDetail.as_view(), name="detail"),
    path("<int:pk>/edit/", views.EditFundingView.as_view(), name="edit"),
    path("search/", views.SearchView.as_view(), name="search"),
]
