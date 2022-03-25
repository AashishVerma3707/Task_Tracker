from celery import shared_task
from django.core.mail import send_mail
from models import Task,CustomUser

@shared_task
def sleepi(duration):
    sleep(duration)
    return None



@shared_task
def send_mail_task():
    l1,l2=[],[]
    obj=Task.objects.all()
    for i in obj:
        l1.append(i.status)
    message_body=l1
    subject="status update"
    mail="aashish3707a@gmail.com"
    obj2=CustomUser.objects.get(Team_leader=True)
    for i in obj2:
        l2.append(i.Email)
    send_mail(subject,message_body,mail,l2,fail_silently=False)
    return None