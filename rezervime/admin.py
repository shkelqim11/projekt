
# Register your models here.
from django.contrib import admin
from .models import *


@admin.register(Rezervim)
class RezervimAdmin(admin.ModelAdmin):
    list_display = ("emri", "telefoni", "sherbimi", "data", "ora", "status", "krijuar_me")
    list_filter = ("status", "sherbimi", "data")
    search_fields = ("emri", "telefoni", "email")
    
@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ("service_name", "service_slug", "service_price")
    search_fields = ("service_name", "service_slug")