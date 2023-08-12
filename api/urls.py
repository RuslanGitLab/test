# Routers provide an easy way of automatically determining the URL conf.
from rest_framework import routers

from api.views import BuyerViewSet, PanViewSet

router = routers.DefaultRouter()
router.register(r'users', BuyerViewSet)
router.register(r'pans', PanViewSet)

urlpatterns = []
urlpatterns.extend(router.urls)
