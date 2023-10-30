from django.shortcuts import render, redirect, HttpResponse

from .tasks import send_sms
from .forms import SmsForm


def sms(request):
    if request.method == "POST":
        form = SmsForm(request.POST)

        if form.is_valid():
            recipient = form.cleaned_data["recipient"]
            message = form.cleaned_data["message"]

            send_sms.delay(recipient, message)
            return redirect("success")

    form = SmsForm()

    return render(request, "sms.html", {"form": form})


def success(request):
    return HttpResponse("<h1>Your message has been send</h1>")
