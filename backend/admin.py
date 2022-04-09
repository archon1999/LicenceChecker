from django.contrib import admin

from .models import ValidAccount


@admin.register(ValidAccount)
class ValidAccountAdmin(admin.ModelAdmin):
    list_display = ['id', 'mac_address', 'host_name']
    search_fields = ['mac_address', 'host_name']
