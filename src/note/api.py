from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from .tasks import send_email_task
from .models import Nota
from arnie.models import Arnia
from apiari.models import Apiario
from .serializers import NotaSerializer


class NotaViewSet(viewsets.ModelViewSet):
    queryset = Nota.objects.all()
    serializer_class = NotaSerializer

    @action(detail=False, url_path='', methods=['get'])
    def send_notes(self, request, *args, **kwargs):
        nota = 'Note test example'
        apiario = get_object_or_404(
            Apiario, apicoltore=request.user, code='666')
        arnia = get_object_or_404(Arnia, apiario=apiario, code='A')
        newnote = Nota(
            arnia=arnia,
            text=nota
        )
        newnote.save()
        send_email_task(nota)
        return Response('Email has been sent')
