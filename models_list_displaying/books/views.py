from django.shortcuts import render, redirect
from django.urls import reverse
from django.core.paginator import Paginator

from books.models import Book


def index(request):
    return redirect(reverse('books'))


def books_view(request):
    template = 'books/books_list.html'
    books = Book.objects.all()

    context = {
        'books': books,
    }
    return render(request, template, context)

def books_view_by_date(request, pub_date=''):
    pub_date_next = ''
    pub_date_previous = ''
    template = 'books/books_list.html'
    books = Book.objects.all().filter(pub_date=pub_date)
    pub_dates = list([str(x[0]) for x in Book.objects.order_by('pub_date').distinct().values_list('pub_date')])
    paginator = Paginator(pub_dates, 1)
    page = paginator.page(paginator.object_list.index(pub_date) + 1)
    if page.has_next():
        pub_date_next = pub_dates[page.number]
    if page.has_previous():
        pub_date_previous = pub_dates[page.number-2]

    context = {
        'books': books,
        'page': page,
        'pub_date': pub_date,
        'pub_date_next': pub_date_next,
        'pub_date_previous': pub_date_previous,
    }
    return render(request, template, context)
