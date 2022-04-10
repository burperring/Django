from django.urls import path
from fundings import views as funding_views

app_name = "core"


urlpatterns = [
    path("", funding_views.HomeView.as_view(), name="home"),
]
