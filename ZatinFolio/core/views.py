from django.http import HttpResponseRedirect
from django.template.response import TemplateResponse
from ..contact.views import send_email_func

from ..contact.forms import ContactForm


# Create your views here.
def home(request):
    form = ContactForm(request.POST or None)
    if form.is_valid():
        message_data = form.cleaned_data
        if send_email_func(request, message_data):
            form.save()
            return HttpResponseRedirect('/')
    ctx = {"form": form}
    return TemplateResponse(
        request,
        "index.html",
        ctx
    )
