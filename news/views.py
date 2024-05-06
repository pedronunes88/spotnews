from django.shortcuts import render

# Create your views here.


def news_home(request):
    news_views = News.objects.all()
    return render(request, "news_home.html", {"news_views": news_views})
