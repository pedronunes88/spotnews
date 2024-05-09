from django.shortcuts import render
from .models import News

# Create your views here.


def news_home(request):
    news = News.objects.all()
    return render(request, "home.html", {"news": news})
