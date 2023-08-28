from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from .tasks import test_func


def test(request):
    test_func.delay()
    return HttpResponse("send")
