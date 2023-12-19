from django.shortcuts import render
from django.http import HttpResponse
from django.db.models.functions import Length

# Create your views here.
from app.models import *
def display_topics(request):
    QLTO=Topic.objects.all()
    QLTO=Topic.objects.all().order_by('topic_name')
    QLTO=Topic.objects.all().order_by('-topic_name')
    QLTO=Topic.objects.all().order_by(Length('topic_name'))
    QLTO=Topic.objects.all().order_by(Length('topic_name').desc())
    d={'QLTO':QLTO}
    return render(request,'display_topics.html',d)

def display_webpage(request):
    QLWO=Webpage.objects.all()
    QLWO=Webpage.objects.all().order_by('name')
    QLWO=Webpage.objects.all().order_by('-name')
    QLWO=Webpage.objects.all().order_by(Length('topic_name'))
    QLWO=Webpage.objects.all().order_by(Length('email').desc())
    QLWO=Webpage.objects.filter(topic_name='cricket').order_by(Length('url').desc())
    QLWO=Webpage.objects.exclude(topic_name='cricket').order_by(Length('url'))
    
    d={'QLWO':QLWO}
    return render(request,'display_webpage.html',d)

def display_accessrecord(request):
    QLAO=AccessRecord.objects.all()
    QLAO=AccessRecord.objects.all().order_by(Length('author'))
    QLAO=AccessRecord.objects.all().order_by(Length('author').desc())
    QLAO=AccessRecord.objects.filter(date='2023-12-07').order_by(Length('author').desc())
    QLAO=AccessRecord.objects.exclude(date='2023-12-07').order_by(Length('author').desc())
    QLAO=AccessRecord.objects.exclude(date='2023-12-07').order_by(Length('author'))
    QLAO=AccessRecord.objects.exclude(date='2023-12-07').order_by('author')
    d={'QLAO':QLAO}
    return render(request,'display_accessrecord.html',d)

def insert_topic(request):
    tn=input('enter topic name: ')
    NTO=Topic.objects.get_or_create(topic_name=tn)[0]
    NTO.save()
    QLTO=Topic.objects.all()
    d={'QLTO':QLTO}
    return render(request,'display_topics.html',d)

def insert_webpage(request):
    tn=input('enter topic name: ')
    n=input('enter name ')
    u=input('enter url ')
    e=input('enter email ')
    TO=Topic.objects.get(topic_name=tn)
    NWO=Webpage.objects.get_or_create(topic_name=TO,name=n,url=u,email=e)[0]
    NWO.save()
    QLWO=Webpage.objects.all()
    d={'QLWO':QLWO}
    return render(request,'display_webpage.html',d)

def insert_access(request):
    pk=int(input('enter pk value of web page '))
    a=input('enter author ')
    date=input('enter date ')
    WO=Webpage.objects.get(pk=pk)
    NAO=AccessRecord.objects.get_or_create(name=WO,author=a,date=date)[0]
    NAO.save()
    QLAO=AccessRecord.objects.all()
    d={'QLAO':QLAO}
    return render(request,'display_accessrecord.html',d)