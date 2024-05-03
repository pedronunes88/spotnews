# req 1 por aqui aparentemente
from django.db import models
from news.validator import validate_even


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
