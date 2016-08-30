from django.http import HttpResponse
from django.template import loader


def index(request):
    return HttpResponse("Hello, world. You're at the securemsg index.")

def genkey(request):
    template = loader.get_template('securemsg/genkey.html')
    context = {}
    return HttpResponse(template.render(context, request))

def addkey(request):
    template = loader.get_template('securemsg/addkey.html')
    context = {}
    return HttpResponse(template.render(context, request))
