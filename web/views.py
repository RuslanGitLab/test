from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from core.models import Pan
from web.forms import PanConfirmDelete


class PanFormView(CreateView):
    model = Pan
    fields = ["price", "vendor", "diameter"]

class PanUpdateView(UpdateView):
    model = Pan
    fields = ["price", "vendor"]
    template_name_suffix = '_update_form'


class PanDeleteView(DeleteView):
    model = Pan
    success_url = reverse_lazy('web:create_pan')
    form_class = PanConfirmDelete