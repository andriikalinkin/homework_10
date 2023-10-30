from django import forms
import phonenumbers


class SmsForm(forms.Form):
    recipient = forms.CharField(label="Enter your phone")
    message = forms.CharField(label="Enter your message")

    def clean_recipient(self):
        cleaned_data = self.cleaned_data.get("recipient")

        try:
            parsed = phonenumbers.parse(cleaned_data, region=None)
        except phonenumbers.NumberParseException as error:
            raise forms.ValidationError(error.args[0])

        return phonenumbers.format_number(parsed, phonenumbers.PhoneNumberFormat.INTERNATIONAL)

    def clean_message(self):
        cleaned_data = self.cleaned_data.get("message")
        if len(cleaned_data) < 30:
            raise forms.ValidationError("Message length should be 30 characters or less")
        return cleaned_data
