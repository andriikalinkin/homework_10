from django.urls import path

from sms import views


urlpatterns = [
    path("sms/", views.sms, name="sms"),
    path("success/", views.success, name="success"),
]
