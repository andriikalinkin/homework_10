from celery import shared_task
from django.conf import settings
from twilio.rest import Client

client = Client(settings.TWILIO_ACCOUNT_SID, settings.TWILIO_AUTH_TOKEN)


@shared_task
def send_sms(recipient, message):
    message = client.messages.create(
        body=message,
        from_="+12183217099",
        to=recipient,
    )

    return message.sid
