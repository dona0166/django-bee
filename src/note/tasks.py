from celery import shared_task
from django.core.mail import send_mail
from django.conf import settings
from time import sleep


@shared_task
def send_email_task(note):
    subject = 'A new note arrived from the Bee Queen'
    message = note
    email_from = settings.EMAIL_HOST_USER
    # taken from temp-mail.org
    recipient_list = ['hitafi8871@seomail.top', ]
    send_mail(subject, message, email_from, recipient_list)

    return None
