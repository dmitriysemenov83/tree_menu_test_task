from django.urls import path

from menu.views import test_view, home_view

urlpatterns = [
    path('', home_view, name='home'),
    path('<slug:slug>/', test_view, name='page'),
    path('<slug:slug>/<slug:subslug>/', test_view, name='subpage'),
]