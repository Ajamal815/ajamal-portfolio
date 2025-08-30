from django.core.mail import send_mail
from django.conf import settings

def send_email(subject, email, message):
    send_mail(subject,message,'ajamalhusain815@gmail.com',[email],fail_silently=False,)