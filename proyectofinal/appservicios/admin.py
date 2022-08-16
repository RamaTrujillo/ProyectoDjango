from django.contrib import admin
from .models import Servicio

class servicioAdmin(admin.ModelAdmin):
    readonly_fields=('created', 'updated',)

admin.site.register(Servicio, servicioAdmin)

# Register your models here.
