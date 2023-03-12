from django.contrib import admin

# Register your models here.
from mptt.admin import MPTTModelAdmin

from fias.models import FIASNode

admin.site.register(FIASNode, MPTTModelAdmin)
