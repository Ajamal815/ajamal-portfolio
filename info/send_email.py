from django.core.mail import send_mail
from django.conf import settings

def send_email(subject, email, message):
    send_mail(subject,message,settings.EMAIL_HOST_USER,[email, 'ajamalhusain815@gmail.com'],fail_silently=False,)