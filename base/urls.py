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
    path('add/', views.add_book, name='add'),
    path('book/<str:id>', views.book, name='book'),
    path('author/<str:id>', views.author, name='author'),
    path('serie/<str:id>', views.serie, name='serie'),
    path('drop/<str:id>', views.drop, name='drop'),
    path('update_user/', views.update_user, name='update_user'),
    path('delete_comment/<str:id>', views.delete_comment, name='delete_comment')

]
