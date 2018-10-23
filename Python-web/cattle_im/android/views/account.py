import json

from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST, require_GET

from android.api.wraper import account


@require_POST
@account.login_wrap
def login(request):
    print(request.POST)
    dic = {
        "status": 0,
        "name": "lkk",
        "avatar": "asfklsajflkdsja",
        "token": "asjfklsjdkfjaslksa"
    }

    return HttpResponse(json.dumps(dic))


@require_POST
@account.register_wrap
def register(request):

    dic = {
        "status": 0,
        "name": "lkk",
        "avatar": "asfklsajflkdsja",
        "token": "asjfklsjdkfjaslksa"
    }

    return HttpResponse(json.dumps(dic))

