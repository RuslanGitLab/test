from django.shortcuts import render
from fias.models import FIASNode


def show_fias(request):
    return render(request, "fias/fias.html", {'fias': FIASNode.objects.all()})
