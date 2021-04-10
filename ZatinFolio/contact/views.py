from django.conf import settings
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from datetime import datetime
# Create your views here.
def send_email_func(request, message_data):
    subject = message_data['subject']
    html_mail = render_to_string('email_contact.html', {'context': message_data,'datetime':datetime.now()})
    plain_message = strip_tags(html_mail)
    email_from = settings.EMAIL_HOST_USER
    recipient_list = ['yinmazatin33@gmail.com', 'yinmazatin21@gmail.com']
    send_mail(
        subject, plain_message, email_from, recipient_list,html_message =html_mail)
    return True
