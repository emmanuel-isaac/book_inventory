from django.shortcuts import render
from django.views.generic import View
from django.http import HttpResponse

from .models import Book


class HomePageView(View):
    def get(self, request):
        books = Book.objects.all()
        return render(request, 'index.html', { 'books': books })
