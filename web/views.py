from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView

from core.models import Pan
from web.forms import PanConfirmDelete, RegisterForm, PanForm



class PanCreateView(LoginRequiredMixin, CreateView):
    model = Pan
    form_class = PanForm

    def get_form_kwargs(self):
        kwargs = super(PanCreateView, self).get_form_kwargs()
        kwargs["request"] = self.request
        return kwargs

    
class PanUpdateView(UpdateView):
    model = Pan
    fields = ["price", "vendor", "creator"]
    template_name_suffix = '_update_form'

    def get_form(self, form_class=None):
        form = super(PanUpdateView, self).get_form(form_class=None)
        form.fields["creator"].disabled = True
        return form


class PanDeleteView(DeleteView):
    model = Pan
    success_url = reverse_lazy('web:create_pan')
    form_class = PanConfirmDelete


@login_required
def profile_view(request):
    return render(request, 'web/profile.html')


class RegisterView(FormView):
    form_class = RegisterForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy("web:profile")
    def form_valid(self, form):
        form.save()
        return super().form_valid(form)