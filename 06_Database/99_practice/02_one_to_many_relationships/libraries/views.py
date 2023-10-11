from django.shortcuts import render, redirect
from .models import Author, Book
from .forms import BookForm

# Create your views here.
def index(request):
    authors = Author.objects.all()
    context = {
        'authors': authors
    }
    return render(request, 'libraries/index.html', context)


def detail(request, pk):
    author = Author.objects.get(pk=pk)
    book_form = BookForm()
    books = author.book_set.all()
    context = {
        'author': author,
        'book_form': book_form,
        'books': books,
    }
    return render(request, 'libraries/detail.html', context)


def create_book(request, author_pk):
    author = Author.objects.get(pk=author_pk)
    book_form = BookForm(request.POST)
    if book_form.is_valid():
        book = book_form.save(commit=False)
        book.author = author
        book_form.save()
        return redirect('libraries:detail', author.pk)
    context = {
        'author': author,
        'book_form': book_form,
    }
    return render(request, 'libraries/detail.html', context)