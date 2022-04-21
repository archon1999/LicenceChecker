from django.contrib import admin
from django.urls import path

from backend.views import (check_valid_account, create_new_account,
                           get_program_version, get_account_program_exe)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('create/', create_new_account),
    path('check/', check_valid_account),
    path('program_version/', get_program_version),
    path('download/', get_account_program_exe)
]
