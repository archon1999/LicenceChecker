from django.contrib import admin

from .models import ValidAccount, ProgramVersion


@admin.register(ValidAccount)
class ValidAccountAdmin(admin.ModelAdmin):
    list_display = ['id', 'mac_address', 'host_name', 'program_version',
                    'created']
    search_fields = ['mac_address', 'host_name']


@admin.register(ProgramVersion)
class ProgramVersionAdmin(admin.ModelAdmin):
    list_display = ['id', 'version', 'created']
