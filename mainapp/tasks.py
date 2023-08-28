from mainapp import models
from celery import shared_task
from django.core.mail import send_mail

from celery_project import settings
@shared_task(bind=True)
def test_func(seld):
    users=models.User.objects.all()
    for user in users:
        print(user)
        mail_subject="hi"
        msg="Hello"
        to_email=user.email
        print(to_email)
        send_mail(subject=mail_subject, message=msg, from_email=settings.EMAIL_HOST_USER ,recipient_list=[to_email],fail_silently=True)

    return "Done"