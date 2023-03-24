from django import forms
from django.contrib.auth.forms import UserCreationForm, PasswordResetForm
from django.core.exceptions import ValidationError

from core.models import Pan, Buyer


class PanForm(forms.ModelForm):
    class Meta:
        model = Pan
        fields = ["price", "vendor", "diameter"]


class PanConfirmDelete(forms.Form):
    confirm_delete = forms.BooleanField(required=False)

    def clean(self):
        if self.cleaned_data["confirm_delete"] is False:
            raise ValidationError("You must confirm this form!")
        return super(PanConfirmDelete, self).clean()


class RegisterForm(forms.ModelForm):
    confirmation = forms.BooleanField()

    class Meta:
        model = Buyer
        fields = ("email", )

    def clean_confirmation(self):
        if self.cleaned_data["confirmation"] is not True:
            raise ValidationError("You must confirm!")
