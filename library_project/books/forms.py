from django import forms
from .models import Book

class BookForm(forms.ModelForm):
    title = forms.CharField(max_length=200, label='Название книги')
    author = forms.CharField(max_length=100, label='Автор')
    description = forms.CharField(widget=forms.Textarea, label='Описание книги')
    published = forms.IntegerField(label='Год публикации')

    class Meta:
        model = Book
        fields = ['title', 'author', 'description', 'published']