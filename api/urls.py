from rest_framework.routers import DefaultRouter

from api.views import BuyerViewSet, PanViewSet

router = DefaultRouter()
router.register("buyers", BuyerViewSet)
router.register("pans", PanViewSet)

urlpatterns = []

urlpatterns.extend(router.urls)
