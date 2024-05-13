# req 1 por aqui aparentemente
from django.db import models
from news.validator import validate_even
from django.core.exceptions import ValidationError
from django.utils import timezone


class Category(models.Model):
    name = models.CharField(max_length=200, validators=[validate_even])

    # aqui antes copilot colocou um campo de descrição, mas não é necessário
    def __str__(self):
        return self.name


class User(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)
    password = models.CharField(max_length=200)
    role = models.CharField(max_length=200)

    def __str__(self):
        return self.name


def validate_title(value):
    if len(value.split()) <= 1:
        raise ValidationError("O título deve conter pelo menos 2 palavras.")


class News(models.Model):
    title = models.CharField(
        max_length=200,
        validators=[validate_title],  # aqui validação personalizada
        null=False,
        blank=False,
    )
    content = models.TextField(null=False, blank=False)
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="news",  # aqui é o relacionamento com o modelo User
        null=False,
    )
    created_at = models.DateField(
        default=timezone.now, null=False, blank=False
    )
    image = models.ImageField(
        upload_to="img/", null=True, blank=True  # aqui localização do upload
    )
    categories = models.ManyToManyField(
        "Category",  # aqui aponta para o modelo Category
        related_name="news",  # aqui é o relacionamento inverso
        blank=False,
    )

    def __str__(self):
        return self.title
