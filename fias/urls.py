from django.urls import path

from fias.views import show_fias

app_name = "fias"

urlpatterns = [
    path("fias/", show_fias, name="show_fias")
]
