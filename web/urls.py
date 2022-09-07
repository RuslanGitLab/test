from django.urls import path
from .views import PanCreateView, PanUpdateView, PanDeleteView
app_name = "web"

urlpatterns = [
    path('pans', PanCreateView.as_view(), name="create_pan"),
    path('pans/<pk>', PanUpdateView.as_view(), name="update_pan"),
    path('pans/<pk>/delete', PanDeleteView.as_view(), name="delete_pan"),
]