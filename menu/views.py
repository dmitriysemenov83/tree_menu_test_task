from django.http import HttpResponse
from django.shortcuts import render


def home_view(request):
    return render(request, 'menu/home.html')


def test_view(request, slug, subslug=None):
    return HttpResponse(f"<h2>Вы на странице: /{slug}/{subslug or ''}</h2>")


