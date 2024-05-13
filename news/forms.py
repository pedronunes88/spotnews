from django import forms
from .models import Category, News, Author


class CategoryForm(forms.Form):
    name = forms.CharField(max_length=200)


from .models import Author, Category


from django import forms
from .models import News


class NewsForm(forms.ModelForm):
    new_categories = forms.CharField(max_length=200, required=False)

    class Meta:
        model = News
        fields = [
            "title",
            "content",
            "author",
            "created_at",
            "image",
            "categories",
        ]

    def clear_categories(self):
        return self.cleaned_data["new_categories"].split(",")
