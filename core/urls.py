from django.contrib import admin
from django.urls import path

from backend.views import create_new_account, check_valid_account

urlpatterns = [
    path('admin/', admin.site.urls),
    path('create/', create_new_account),
    path('check/', check_valid_account),
]
