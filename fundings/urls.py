from django.urls import path
from . import views


app_name = "fundings"

urlpatterns = [path("<int:pk>", views.funding_detail, name="detail")]
