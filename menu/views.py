from django.http import HttpResponse
from django.shortcuts import render


def home_view(request):
    return render(request, 'menu/home.html')


def test_view(request, slug, subslug=None):
    return render(request, 'menu/page.html', {
        'slug': slug,
        'subslug': subslug,
    })


