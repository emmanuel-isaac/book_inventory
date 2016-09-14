from django.shortcuts import render
from django.views.generic import View
from django.http import HttpResponse


class HomePageView(View):
    def get(self, request):
        return HttpResponse(200)
