from django.shortcuts import render, get_object_or_404, redirect
from .models import News, Category, User
from .forms import CategoryForm, NewsForm
from rest_framework import generics, viewsets
from .models import Category
from .serializers import CategorySerializer, UserSerializer


# Create your views here.


def news_home(request):
    news = News.objects.all()
    return render(request, "home.html", {"news": news})


def news_details(request, id):
    news = get_object_or_404(News, id=id)
    return render(request, "news_details.html", {"news": news})


def categories_form(request):
    # primeiro vamo de um formulário vazio
    clear_form = CategoryForm()

    # depois vamo checar se a requisição é do tipo POST
    if request.method == "POST":
        # ai vamo criar um formulário com os dados da requisição
        clear_form = CategoryForm(request.POST)

        # com isso vamo ver se o formulário é válido
        if clear_form.is_valid():
            # ai vem uma nova instância do modelo Category com os dados do formulário e salva no banco de dados
            Category.objects.create(**clear_form.cleaned_data)

            # depois o retorno pro usuário para a página inicial após o cadastro bem-sucedido
            return redirect("home-page")

    # pra ver o formulário ser exibido no template
    general = {"form": clear_form}
    return render(request, "categories_form.html", general)


def news_form(request):
    clear_form = NewsForm()
    if request.method == "POST":
        clear_form = NewsForm(request.POST, request.FILES)
        if clear_form.is_valid():
            clear_form.save()
        return redirect("home-page")
    else:
        clear_form = NewsForm()
        users = User.objects.all()
        categories = Category.objects.all()
        general = {
            "form": clear_form,
            "users": users,
            "categories": categories,
        }
        return render(request, "news_form.html", general)


class CategoryList(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class UserListView(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
