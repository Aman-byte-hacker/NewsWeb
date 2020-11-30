from django.shortcuts import render

# Create your views here.

def IndiaNews(request):
    import requests
    import json
    news_api=requests.get('http://newsapi.org/v2/top-headlines?country=in&apiKey=d4008e8fdd0f4ab3b57ee804ec009671')
    api=json.loads(news_api.content)
    return render(request,"index.html",{'api':api})

def tech(request):
    import requests
    import json
    tech_api= requests.get('http://newsapi.org/v2/top-headlines?country=in&category=technology&apiKey=d4008e8fdd0f4ab3b57ee804ec009671')
    techapi=json.loads(tech_api.content)
    return render(request,"tech.html",{'techapi':techapi})

def entertainment(request):
    import requests
    import json
    entertain_api=requests.get('http://newsapi.org/v2/top-headlines?country=in&category=entertainment&apiKey=d4008e8fdd0f4ab3b57ee804ec009671')
    entertainapi=json.loads(entertain_api.content)
    return render(request,"entertain.html",{'entertainapi':entertainapi})

def sport(request):
    import requests
    import json
    sport_api=requests.get('http://newsapi.org/v2/top-headlines?country=in&category=sports&apiKey=d4008e8fdd0f4ab3b57ee804ec009671')
    sportapi=json.loads(sport_api.content)
    return render(request,"sport.html",{'sportapi':sportapi})

def science(request):
    import requests
    import json
    science_api=requests.get('http://newsapi.org/v2/top-headlines?country=in&category=science&apiKey=d4008e8fdd0f4ab3b57ee804ec009671')
    scienceapi=json.loads(science_api.content)
    return render(request,"science.html",{'scienceapi':scienceapi})

def health(request):
    import requests
    import json
    health_api=requests.get('http://newsapi.org/v2/top-headlines?country=in&category=health&apiKey=d4008e8fdd0f4ab3b57ee804ec009671')
    healthapi=json.loads(health_api.content)
    return render(request,"health.html",{'healthapi':healthapi})