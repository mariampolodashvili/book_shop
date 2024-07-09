from django.urls import path
from . import views

from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('books', views.books, name='books'),
    path('about/', views.about, name='about'),
    path('series/', views.series, name='series'),
    path('authors/', views.authors, name='authors'),
    path('profile/<str:pk>', views.profile, name='profile'),
    path('adding/<int:id>', views.adding, name='adding'),
    path('delete/<int:id>', views.delete, name='delete'),
    path('login_user/', views.login_user, name="login"),
    path('logout_user/', views.logout_user, name="logout"),
    path('registration/', views.registration, name="registration"),
    path('add/', views.add_book, name='add')
]
