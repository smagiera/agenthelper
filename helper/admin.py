from django.contrib import admin

from .models import *

admin.site.register(Vehicle)
admin.site.register(Client)
admin.site.register(Policy)
admin.site.register(Insurer)

# Register your models here.
