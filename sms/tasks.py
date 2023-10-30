from celery import shared_task
from django.conf import settings
from twilio.rest import Client

client = Client(settings.TWILIO_ACCOUNT_SID, settings.TWILIO_AUTH_TOKEN)


@shared_task
def send_sms(recipient, message):
    print("Hello, Celery!")

    message = client.messages.create(
        body=message,  # "Hello from outer space!"
        from_="+12183217099",
        to=recipient  # "+4796869214"
    )

    return message.sid
