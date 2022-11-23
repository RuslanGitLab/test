from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError

from core.models import Pan, Buyer


class PanForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop("request")
        super(PanForm, self).__init__(*args, **kwargs)

    class Meta:
        model = Pan
        fields = ["price", "vendor", "diameter"]

    def save(self, commit=True):
        pan = super(PanForm, self).save(commit=commit)
        pan.creator = self.request.user
        pan.save()
        return pan


class PanConfirmDelete(forms.Form):
    confirm_delete = forms.BooleanField(required=False)

    def clean(self):
        if self.cleaned_data["confirm_delete"] is False:
            raise ValidationError("You must confirm this form!")
        return super(PanConfirmDelete, self).clean()


class RegisterForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = Buyer
        fields = UserCreationForm.Meta.fields + ("email", )
