from django.shortcuts import render
from django.http import HttpResponse
from .tasks import send_email_task
from .models import Nota
from arnie.models import Arnia
from apiari.models import Apiario
from django.shortcuts import get_object_or_404

# Create your views here.


def index(request):
    nota = 'Note test example'
    apiario = get_object_or_404(Apiario, code='666')
    arnia = get_object_or_404(Arnia, apiario=apiario, code='A')
    newnote = Nota(
        arnia=arnia,
        text=nota
    )
    newnote.save()
    send_email_task(nota)
    return HttpResponse('<h1>Email has been sent</h1>')
