from django.db import models
from django.utils.translation import gettext as _
from mptt.fields import TreeForeignKey
from mptt.models import MPTTModel


class FIASNode(MPTTModel):
    HOUSE_TYPE = "house"
    STREET_TYPE = "street"
    CITY_DISTRICT_TYPE = "city_district"
    CITY_TYPE = "city"
    FEDERAL_DISTRICT_TYPE = "federal_district"
    COUNTRY = "country"

    type_choices = [
        (HOUSE_TYPE, _("house")),
        (STREET_TYPE, _("street")),
        (CITY_DISTRICT_TYPE, _("city district")),
        (CITY_TYPE, _("city")),
        (FEDERAL_DISTRICT_TYPE, _("federal district")),
        (COUNTRY, _("country")),
    ]
    name = models.CharField(max_length=100, help_text=_("Name of FIAS node."))
    type = models.CharField(
        choices=type_choices, max_length=50, help_text=_("FIAS node type")
    )
    parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')

    class MPTTMeta:
        order_insertion_by = ['name']

    def __str__(self):
        return f"{self.type}: {self.name}"
