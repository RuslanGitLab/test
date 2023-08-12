from rest_framework import viewsets

from core.models import Buyer, Pan
from api.serializers import BuyerSerializer, PanSerializer


class BuyerViewSet(viewsets.ModelViewSet):
    queryset = Buyer.objects.all()
    serializer_class = BuyerSerializer


class PanViewSet(viewsets.ModelViewSet):
    queryset = Pan.objects.all()
    serializer_class = PanSerializer
