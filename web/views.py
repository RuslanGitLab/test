from django.shortcuts import render

# Create your views here.
from django.views.generic import FormView

from core.forms import BuyerForm


class BuyerFormView(FormView):
    template_name = 'web/buyer.html'
    form_class = BuyerForm
    success_url = '/web/buyer'
