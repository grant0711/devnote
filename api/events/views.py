import logging

from django.core.exceptions import ValidationError
from django.db import IntegrityError
from django.http import JsonResponse
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view
from rest_framework.decorators import parser_classes
from rest_framework.parsers import JSONParser

from events.models import DevNote

logger = logging.getLogger('logger')


@api_view(['GET'])
def home(request):
    return JsonResponse({"msg": "okay"}, status=200)



@api_view(['POST'])
@parser_classes([JSONParser])
def event(request):
    logger.info(f"Incoming event: {request.data}")
    
    try:
        devnote = DevNote.objects.filter(user=request.user, date=request.data.get('date', '')).first()
        if not devnote:
            devnote = DevNote.objects.create(
                user=request.user,
                content=request.data.get('content', ''),
                date=request.data.get('date', '')
            )
            return JsonResponse({"msg": f"created new devnote for {devnote.date}"}, status=200)
        else:
            devnote.content = request.data.get('content', '')
            devnote.save()
            return JsonResponse({"msg": f"updated devnote for {devnote.date}"}, status=200)
    except ValidationError as e:
        return JsonResponse({"msg": e.__repr__()}, status=400)
    except IntegrityError as e:
        return JsonResponse({"msg": e.__repr__()}, status=400)