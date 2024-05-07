from django.shortcuts import render
from .models import News

# Create your views here.


def news_home(request):
    news = News.objects.all()
    return render(request, "news_home.html", {"news": news})
