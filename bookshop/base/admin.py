from django.contrib import admin
from .models import Book, Author, User, Bestsellers, Series, Genre, Comment


admin.site.register(Book)
admin.site.register(Author)
admin.site.register(User)
admin.site.register(Bestsellers)
admin.site.register(Series)
admin.site.register(Genre)
admin.site.register(Comment)
