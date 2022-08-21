from django.http import HttpResponse


# Create your views here.
from rest_framework.generics import get_object_or_404
from rest_framework.viewsets import ViewSet

from core.models import Buyer
from core.serializers import UserViewSetInputSerializer


def square_of_a(request):
    a = request.GET.get("a")
    if str(a).isdigit():
        return HttpResponse(content=f"Aaa in square is {int(a) ** 2}")
    return HttpResponse(content=f"Aaa is not a digit, or not presented")


class UserViewSet(ViewSet):
    def purchases(self, request):
        params_serializer = UserViewSetInputSerializer(data=request.query_params)
        params_serializer.is_valid(raise_exception=True)

        user_id = params_serializer.validated_data["user_id"]

        user = get_object_or_404(Buyer, pk=user_id)

        # purchases = user.