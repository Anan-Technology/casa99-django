from django import forms
from django.utils.translation import pgettext, pgettext_lazy
from ..contact.models import ContactInfo


class ContactForm(forms.ModelForm):
    name = forms.CharField(
        label=pgettext("Name", "Name")
    )
    email = forms.EmailField(
        label=pgettext("Email", "Email")
    )
    subject = forms.CharField(
        label=pgettext("Subject", "Subject")
    )
    message = forms.TextInput(
        attrs={'size': 5, 'Message': 'Message'}
    )

    class Meta:
        model = ContactInfo
        fields = ["name", "email", "subject", "message"]
