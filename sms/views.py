from django.shortcuts import render, redirect

from .tasks import send_sms
from .forms import SmsForm


def sms(request):
    # send_sms.delay(recipient, message)
    # pass
    # return render(request, "sms.html", {"data":data})

    if request.method == 'POST':
        form = SmsForm(request.POST)

        if form.is_valid():
            recipient = form.cleaned_data['recipient']
            message = form.cleaned_data['message']

            send_sms.delay(recipient, message)
            return redirect('success_page')  # Перенаправляем пользователя на страницу успешной отправки

    form = SmsForm()

    return render(request, "sms.html", {"form": form})
