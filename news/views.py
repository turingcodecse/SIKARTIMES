from audioop import reverse
from unicodedata import category
from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse,HttpResponseRedirect
from django.urls import reverse
from . models import News,Photo,Video,Magazine,Logo

def index(request):
    template = loader.get_template('index.html')
    news = News.objects.filter(status=1).order_by('-id').values()
    try:
        magazine = Magazine.objects.filter(status=1).last()
        top_1 = news[0] #top 1 news
        top_news = news[1:5] #top 2nd last to 5th last news
        
        
        #top 5 news id
        top_news_id = []
        top_news_id.append(top_1['id'])
        for x in top_news:
            top_news_id.append(x['id'])
        

        top_1 = News.objects.get(id=top_1['id'])

        #top 4 national news (not include in above top 5 news)
        national_news = News.objects.filter(type='National',status=1).order_by('-id').values()
        top_national_news = national_news[0:4]

        #top 4 politics news (not include in above top 5 news)
        politics_news = News.objects.filter(type='Politics',status=1).order_by('-id').values()
        top_politics_news = politics_news[0:4]

        #top 2 sports news(not include in above top 5 news)
        sports_news = News.objects.filter(type='Sports',status=1).order_by('-id').values()
        top_sports_news = sports_news[0:4]

        #top 1 carrier news
        top_carrier_news = News.objects.filter(type='Carrier',status=1).last()
        top_carrier_news_image = str(top_carrier_news.image)
        top_carrier_news_image = top_carrier_news_image[4:]

        #top 1 International news
        top_international_news = News.objects.filter(type='InterNational',status=1).last()
        top_international_news_image = str(top_international_news.image)
        top_international_news_image = top_international_news_image[4:]

        #top 1 entertainment news
        top_entertainment_news = News.objects.filter(type='Entertainment',status=1).last()
        top_entertainment_news_image = str(top_entertainment_news.image)
        top_entertainment_news_image = top_entertainment_news_image[4:]

        #top 1 Rajasthan news
        top_rajasthan_news = News.objects.filter(type='Rajasthan',status=1).last()
        top_rajasthan_news_image = str(top_rajasthan_news.image)
        top_rajasthan_news_image = top_rajasthan_news_image[4:]

        video = Video.objects.filter(status=1).order_by('-id').values()

        logo = Logo.objects.last()

        context = {
            'news' : news,
            'top_1' : top_1,
            'magazine': magazine,
            'top_news' : top_news,
            'top_national_news' : top_national_news,
            'top_politics_news' : top_politics_news,
            'top_sports_news' : top_sports_news,
            'top_carrier_news' : top_carrier_news,
            'top_international_news' : top_international_news,
            'top_international_news' : top_international_news,
            'top_entertainment_news' : top_entertainment_news,
            'top_rajasthan_news' : top_rajasthan_news,
            'top_carrier_news_image' : top_carrier_news_image,
            'top_international_news_image' : top_international_news_image,
            'top_entertainment_news_image' : top_entertainment_news_image,
            'top_rajasthan_news_image' : top_rajasthan_news_image,
            'video' : video,
            'logo' : logo,
        }
        return HttpResponse(template.render(context,request))
    except:
        context = {
        }
        return HttpResponse(template.render(context,request))

def national(request):
    template = loader.get_template('news.html')
    news = News.objects.filter(type='National',status=1).order_by('-id').values()
    magazine = Magazine.objects.filter(status=1).last()
    logo = Logo.objects.last()
    context = {
        'news':news,
        'type' : 'देश',
        'magazine' : magazine,
        'logo' : logo,
    }
    return HttpResponse(template.render(context,request))

def sikar(request):
    template = loader.get_template('news.html')
    news = News.objects.filter(type='Sikar',status=1).order_by('-id').values()
    magazine = Magazine.objects.filter(status=1).last()
    logo = Logo.objects.last()
    context = {
        'news':news,
        'type' : 'सीकर',
        'magazine' : magazine,
        'logo' : logo,
    }
    return HttpResponse(template.render(context,request))

def international(request):
    template = loader.get_template('news.html')
    news = News.objects.filter(type='InterNational',status=1).order_by('-id').values()
    magazine = Magazine.objects.filter(status=1).last()
    logo = Logo.objects.last()
    context = {
        'news':news,
        'type' : 'इंटरनेशनल',
        'magazine' : magazine,
        'logo' : logo,
    }
    return HttpResponse(template.render(context,request))

def rajasthan(request):
    template = loader.get_template('news.html')
    news = News.objects.filter(type='Rajasthan',status=1).order_by('-id').values()
    magazine = Magazine.objects.filter(status=1).last()
    logo = Logo.objects.last()
    context = {
        'news':news,
        'type' : 'राजस्थान',
        'magazine' : magazine,
        'logo' : logo,
    }
    return HttpResponse(template.render(context,request))

def politics(request):
    template = loader.get_template('news.html')
    news = News.objects.filter(type='Politics',status=1).order_by('-id').values()
    magazine = Magazine.objects.filter(status=1).last()
    logo = Logo.objects.last()
    context = {
        'news':news,
        'type' : 'राजनीति',
        'magazine' : magazine,
        'logo' : logo,
    }
    return HttpResponse(template.render(context,request))

def sports(request):
    template = loader.get_template('news.html')
    news = News.objects.filter(type='Sports',status=1).order_by('-id').values()
    magazine = Magazine.objects.filter(status=1).last()
    logo = Logo.objects.last()
    context = {
        'news':news,
        'type' : 'स्पोर्ट्स',
        'magazine' : magazine,
        'logo' : logo,
    }
    return HttpResponse(template.render(context,request))

def entertainment(request):
    template = loader.get_template('news.html')
    news = News.objects.filter(type='Entertainment',status=1).order_by('-id').values()
    magazine = Magazine.objects.filter(status=1).last()
    logo = Logo.objects.last()
    context = {
        'news':news,
        'type' : 'मनोरंजन',
        'magazine' : magazine,
        'logo' : logo,
    }
    return HttpResponse(template.render(context,request))

def carrier(request):
    template = loader.get_template('news.html')
    news = News.objects.filter(type='Carrier',status=1).order_by('-id').values()
    magazine = Magazine.objects.filter(status=1).last()
    logo = Logo.objects.last()
    context = {
        'news':news,
        'type' : 'करिअर',
        'magazine' : magazine,
        'logo' : logo,
    }
    return HttpResponse(template.render(context,request))

def contact(request):
    logo = Logo.objects.last()
    template = loader.get_template('contact.html')
    context = {
        'logo':logo,
    }
    return HttpResponse(template.render(context,request))

def photo(request):
    template = loader.get_template('photo.html')
    photo = Photo.objects.all().order_by('-id').values()
    logo = Logo.objects.last()
    context = {
        'photo':photo,
        'logo' : logo,
    }
    return HttpResponse(template.render(context,request))

def video(request):
    template = loader.get_template('video.html')
    video = Video.objects.all().order_by('-id').values()
    logo = Logo.objects.last()
    context = {
        'video':video,
        'logo' : logo,
    }
    return HttpResponse(template.render(context,request))

def magazine(request):
    template = loader.get_template('magazine.html')
    magazine = Magazine.objects.filter(status=1).order_by('-id').values()
    logo = Logo.objects.last()
    context = {
        'magazine':magazine,
        'logo' : logo,
    }
    return HttpResponse(template.render(context,request))


def news_description(request,news_des):
    template = loader.get_template('full_news.html')
    fullnews = News.objects.filter(news_slug=news_des).values()
    magazine = Magazine.objects.all().last()
    logo = Logo.objects.last()
    context = {
        'fullnews' : fullnews,
        'magazine' : magazine,
        'logo' : logo,
    }
    return HttpResponse(template.render(context,request))

def error_404(request,exception):
    template = loader.get_template('404.html')
    return HttpResponse(template.render({},request))
