from django.urls import path
from . import views


app_name = "buys"

urlpatterns = [
    path("get/<int:funding>/", views.BuyFundingView.as_view(), name="get"),
    path("myfunding/", views.SeeMyBuyFunding.as_view(), name="myfunding"),
]
