from django.shortcuts import render
from .tasks import add


def sms(request):
    add.delay(1, 2)
    return render(request, "sms.html")
