from django.shortcuts import render
from django.views.generic import View
from django.http import HttpResponse

from .models import Book
from .forms import SearchForm


class HomePageView(View):
    books = Book.objects.all()
    search_form = SearchForm()

    def get(self, request):
        return render(request, 'index.html', {'books': self.books, 'search_form': self.search_form})

    def post(self, request):
        form = SearchForm(request.POST)
        if form.is_valid():
            search_term = form.data.get('search_term')
            category_matches = list(self.get_category_matches(Book, search_term))
            book_title_matches = list(self.get_book_title_matches(Book, search_term))
            all_matches = list(set(category_matches + book_title_matches))
            return render(request, 'index.html',
                          {'matches': all_matches, 'books': self.books, 'search_form': self.search_form})
        return render(request, 'index.html', {'books': self.books, 'search_form': self.search_form})

    @staticmethod
    def get_category_matches(model, search_term):
        return getattr(model, 'objects').filter(category__name__icontains=search_term)

    @staticmethod
    def get_book_title_matches(model, search_term):
        return getattr(model, 'objects').filter(title__icontains=search_term)
