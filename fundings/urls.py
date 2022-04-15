from django.urls import path
from . import views


app_name = "fundings"

urlpatterns = [
    path("<int:pk>", views.FundingDetail.as_view(), name="detail"),
    path("search/", views.SearchView.as_view(), name="search"),
]
