from django.urls import path
from django.views.generic import RedirectView
from . import views


urlpatterns = [
    path('index/', views.home),
    path('home/', views.displayTable, name="home"),
    path('form/<int:id>', views.BookShit),
    path("", RedirectView.as_view(url='index/'))
]
