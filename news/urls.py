from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    news_home,
    news_details,
    categories_form,
    news_form,
    CategoryList,
    UserListView,
)

router = DefaultRouter()
# Registro da rota categories
router.register(r"categories", CategoryList, basename="categories")
router.register(r"users", UserListView, basename="users")


urlpatterns = [
    path("", news_home, name="home-page"),
    path("news/<int:id>/", news_details, name="news-details-page"),
    path("categories/", categories_form, name="categories-form"),
    path("news/", news_form, name="news-form"),
    # Incluindo as URLs geradas pelo roteador
    path("api/", include(router.urls)),
]
