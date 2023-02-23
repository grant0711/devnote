
from django.http import JsonResponse
from rest_framework.decorators import api_view

@api_view(['GET'])
def home(request):
    return JsonResponse({"msg": "okay"}, status=200)



# Fixme remove these as they just add untested lines to views to ensure test
# coverage working on CI
def here_is_a_dummy_function():
    print('it doesnt do anything')

    for i in range(10):
        if i == 100:
            print('yes!')

    return True

def here_is_another():
    for i in range(100):
        k = i / 2

    try:
        i = 5
    except Exception:
        pass

    return False