from django.http.response import JsonResponse

from .models import ValidAccount


def check_valid_account(request):
    mac_address = request.GET.get('mac_address')
    host_name = request.GET.get('host_name')
    is_valid = ValidAccount.accounts.filter(
        mac_address=mac_address,
        host_name=host_name,
    ).exists()
    return JsonResponse({'is_valid': is_valid})


def create_new_account(request):
    mac_address = request.GET.get('mac_address')
    host_name = request.GET.get('host_name')
    ValidAccount.accounts.create(
        mac_address=mac_address,
        host_name=host_name,
    )
    return JsonResponse({'success': True})
