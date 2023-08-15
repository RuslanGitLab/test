from rest_framework import viewsets


# Create your views here.
from api.serializers import BuyerSerializer, PanSerializer
from core.models import Buyer, Pan


class BuyerViewSet(viewsets.ModelViewSet):
    serializer_class = BuyerSerializer
    queryset = Buyer.objects.filter(is_active=True)


class PanViewSet(viewsets.ModelViewSet):
    serializer_class = PanSerializer
    queryset = Pan.objects.all()
