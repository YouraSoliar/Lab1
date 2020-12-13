from django.shortcuts import render
from django.http import JsonResponse

# Create your views here.
from datetime import datetime
import random
import os

def main(request):
    return render(request, 'templates.html', {'parameter': "test"})

def health(request):
    response = {
        'date': datetime.now().isoformat(),
        'current_page': request.build_absolute_uri(),
        'name_of_server': 'Lab3',
        'info_about_server': {
            'system': os.name,
            'srv_pid': os.getpid(),
        },
        'info_about_client': {
            'user agent': request.META['HTTP_USER_AGENT'],
            'remote addr': request.META['REMOTE_ADDR'],
            'remote host': request.META['REMOTE_HOST'],
        }
    }
    return JsonResponse(response)