from django.forms import ModelForm

from core.models import Buyer


class BuyerForm(ModelForm):
    class Meta:
        model = Buyer
        fields = ["username", "email", "password"]