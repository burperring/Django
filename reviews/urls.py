from django.urls import path
from . import views


app_name = "reviews"

urlpatterns = [
    path("create/<int:music>", views.CreateReviewView.as_view(), name="create")
]
