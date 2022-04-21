from django.http.response import JsonResponse, FileResponse, HttpResponse

from .models import ValidAccount, ProgramVersion


def check_valid_account(request):
    mac_address = request.GET.get('mac_address')
    host_name = request.GET.get('host_name')
    is_valid = ValidAccount.accounts.filter(
        mac_address=mac_address,
        host_name=host_name,
    ).exists()
    return JsonResponse({'is_valid': is_valid})


def get_last_program_version():
    return ProgramVersion.programs.order_by('id').last()


def create_new_account(request):
    mac_address = request.GET.get('mac_address')
    host_name = request.GET.get('host_name')
    token = request.GET.get('token')
    if token == 'CPython.uz':
        ValidAccount.accounts.get_or_create(
            mac_address=mac_address,
            host_name=host_name,
            program_version=get_last_program_version(),
        )
        return JsonResponse({'success': True})
    else:
        return JsonResponse({'success': False})


def get_program_version(request):
    mac_address = request.GET.get('mac_address')
    host_name = request.GET.get('host_name')
    if (account := ValidAccount.accounts.filter(
        mac_address=mac_address,
        host_name=host_name
    ).first()):
        return JsonResponse({
            'success': True,
            'program_version': account.program_version.version,
        })
    return JsonResponse({'success': False})


def get_account_program_exe(request):
    mac_address = request.GET.get('mac_address')
    host_name = request.GET.get('host_name')
    if (account := ValidAccount.accounts.filter(
        mac_address=mac_address,
        host_name=host_name
    ).first()):
        filename = account.program_version.exe.name
        return FileResponse(open(filename, 'rb'))
    else:
        return HttpResponse('Error')
