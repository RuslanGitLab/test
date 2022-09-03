from django.urls import path
from .views import *
app_name = "web"

urlpatterns = [
    path("buyer/", BuyerFormView.as_view(), name="buyer")
]
