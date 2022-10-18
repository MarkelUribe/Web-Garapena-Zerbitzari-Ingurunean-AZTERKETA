from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from .models import *

def index(request):
  template = loader.get_template('homepage.html')
  return HttpResponse(template.render())



def kotxeak(request):
    kotxeak = Kotxea.objects.all().values()
    alokairuak = Alokairua.objects.all().values()
    pertsonak = Pertsona.objects.all().values()
    template = loader.get_template('kotxeak.html')
    context = {
        'kotxeak': kotxeak,
        'alokairuak': alokairuak,
        'pertsonak': pertsonak,
    }
    return HttpResponse(template.render(context, request))

def addkotxe(request):
    template = loader.get_template('gehitukotxea.html')
    return HttpResponse(template.render({}, request))

def addrecordkotxe(request):
    x = request.POST['izena']
    y = request.POST['prezioa']
    kotxe = Kotxea(izena=x, prezioa=y)
    kotxe.save()
    return HttpResponseRedirect(reverse('kotxeak'))
  
def deletekotxe(request, id):
    kotxea = Kotxea.objects.get(id=id)
    kotxea.delete()
    return HttpResponseRedirect(reverse('kotxeak'))


def kotxeaalokatu(request):
    kotxeak = Kotxea.objects.all().values()
    pertsonak = Pertsona.objects.all().values()
    alokairuak = Alokairua.objects.all().values()
    template = loader.get_template('kotxeaalokatu.html')
    
    context = {
        'kotxeak': kotxeak,
        'pertsonak': pertsonak,
        'alokairuak': alokairuak,
    }
    return HttpResponse(template.render(context, request))

def kotxeaalokatutodb(request):
    kotxeaid = request.POST['kotxea']
    pertsonaid = request.POST['pertsona']
    alokatuData = request.POST['alokatuData']
    aamaieraData = request.POST['aamaieraData']
    
    kotxeaobj = Kotxea.objects.get(id=kotxeaid)
    alokatzaileaobj = Pertsona.objects.get(id=pertsonaid)
    
    alokairua = Alokairua(alokatuData=alokatuData, aamaieraData=aamaieraData, kotxea=kotxeaobj, alokatzailea=alokatzaileaobj)
    alokairua.save()
    return HttpResponseRedirect(reverse('kotxeak'))

def alokatuamaitu(request, id):
    alokairu = Alokairua.objects.get(id=id)
    alokairu.delete()
    return HttpResponseRedirect(reverse('kotxeak'))


def pertsonak(request):
    pertsonak = Pertsona.objects.all().values()
    template = loader.get_template('pertsonak.html')
    context = {
        'pertsonak': pertsonak,
    }
    return HttpResponse(template.render(context, request))

def addpertsona(request):
    template = loader.get_template('gehitupertsona.html')
    return HttpResponse(template.render({}, request))

def addrecordpertsona(request):
    x = request.POST['izena']
    y = request.POST['tlf']
    pertsona = Pertsona(izena=x, tlf=y)
    pertsona.save()
    return HttpResponseRedirect(reverse('pertsonak'))
  
def deletepertsona(request, id):
    pertsona = Pertsona.objects.get(id=id)
    pertsona.delete()
    return HttpResponseRedirect(reverse('pertsonak'))