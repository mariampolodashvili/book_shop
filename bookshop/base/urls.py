from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('books', views.books, name='books'),
    path('about/', views.about, name='about'),
    path('series/', views.series, name='series'),
    path('authors/', views.authors, name='authors'),
    path('profile/<str:pk>', views.profile, name='profile'),

]