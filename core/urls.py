from django.urls import path
from .views import square_of_a
app_name = "core"


urlpatterns = [
    path('square_of_a', square_of_a)
]
