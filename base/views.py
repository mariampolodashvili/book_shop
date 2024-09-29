from django.shortcuts import render, redirect, get_object_or_404
from .models import Book, User, Bestsellers, Series, Author, Genre, Comment, Price, Categories
from django.db.models import Q
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .forms import MyUserCreationForm, BookForm, UserForm
# from .seeder import seeder_dunc
from django.contrib import messages

def home(request):
    search = request.GET.get("search") if request.GET.get('search') != None else ''
    # seeder_dunc()
    if search:
        price_range = request.GET.get("price_range", None)

        price_ranges = {
            "0-10": (0, 10),
            "10-15": (10, 15),
            "15-20": (15, 20),
            "20-25": (20, 25),
            "25-50": (25, 50),
        }

        books = Book.objects.filter(
            Q(name__icontains=search) | Q(author__name__icontains=search) | Q(genre__name__icontains=search) | Q(categories__name__icontains=search) ).distinct()

        if price_range and price_range in price_ranges:
            min_price, max_price = price_ranges[price_range]
            books = books.filter(price__price__gte=min_price, price__price__lte=max_price)

        genres = Genre.objects.all()
        categories = Categories.objects.all()


        context = {
            "books": books,
            "genres": genres,
            "categories": categories,
            "price_ranges": price_ranges,
            "selected_price_range": price_range
        }

        return render(request, 'base/books.html', context)
    else:
        bestseller_books = Bestsellers.objects.prefetch_related('books').all()
        context = {"bestseller_books": bestseller_books}
        return render(request, 'base/home.html', context)



def books(request):
    search = request.GET.get("search", "")
    price_range = request.GET.get("price_range", None)

    price_ranges = {
        "0-10": (0, 10),
        "10-15": (10, 15),
        "15-20": (15, 20),
        "20-25": (20, 25),
        "25-50": (25, 50),
    }

    books = Book.objects.filter( Q(name__icontains=search) | Q(author__name__icontains=search) | Q(genre__name__icontains=search) |  Q(categories__name__icontains=search) ).distinct()

    if price_range and price_range in price_ranges:
        min_price, max_price = price_ranges[price_range]
        books = books.filter(price__price__gte=min_price, price__price__lte=max_price)

    genres = Genre.objects.all()
    categories = Categories.objects.all()


    context = {
        "books": books,
        "genres": genres,
        "categories": categories,
        "price_ranges": price_ranges,
        "selected_price_range": price_range
    }

    return render(request, 'base/books.html', context)


def series(request):
    search = request.GET.get("search", "")
    if search:
        price_range = request.GET.get("price_range", None)

        price_ranges = {
            "0-10": (0, 10),
            "10-15": (10, 15),
            "15-20": (15, 20),
            "20-25": (20, 25),
            "25-50": (25, 50),
        }

        books = Book.objects.filter(
            Q(name__icontains=search) | Q(author__name__icontains=search) | Q(genre__name__icontains=search) | Q(categories__name__icontains=search) ).distinct()

        if price_range and price_range in price_ranges:
            min_price, max_price = price_ranges[price_range]
            books = books.filter(price__price__gte=min_price, price__price__lte=max_price)

        genres = Genre.objects.all()
        categories = Categories.objects.all()


        context = {
            "books": books,
            "genres": genres,
            "categories": categories,
            "price_ranges": price_ranges,
            "selected_price_range": price_range
        }

        return render(request, 'base/books.html', context)
    else:
        series=Series.objects.all()
        context={"series" : series}
        return render(request, 'base/series.html', context)

def authors(request):
    search = request.GET.get("search") if request.GET.get('search') != None else ''
    if search:
        price_range = request.GET.get("price_range", None)

        price_ranges = {
            "0-10": (0, 10),
            "10-15": (10, 15),
            "15-20": (15, 20),
            "20-25": (20, 25),
            "25-50": (25, 50),
        }

        books = Book.objects.filter(
            Q(name__icontains=search) | Q(author__name__icontains=search) | Q(genre__name__icontains=search) | Q(categories__name__icontains=search)).distinct()

        if price_range and price_range in price_ranges:
            min_price, max_price = price_ranges[price_range]
            books = books.filter(price__price__gte=min_price, price__price__lte=max_price)

        genres = Genre.objects.all()
        categories = Categories.objects.all()

        context = {
            "books": books,
            "genres": genres,
            "categories": categories,
            "price_ranges": price_ranges,
            "selected_price_range": price_range
        }

        return render(request, 'base/books.html', context)
    else:
        authors=Author.objects.all()
        context = {"authors": authors}
        return render(request, 'base/authors.html', context)

def about(request):
    search = request.GET.get("search") if request.GET.get('search') != None else ''
    if search:
        price_range = request.GET.get("price_range", None)

        price_ranges = {
            "0-10": (0, 10),
            "10-15": (10, 15),
            "15-20": (15, 20),
            "20-25": (20, 25),
            "25-50": (25, 50),
        }

        books = Book.objects.filter(
            Q(name__icontains=search) | Q(author__name__icontains=search) | Q(genre__name__icontains=search) | Q(categories__name__icontains=search)).distinct()

        if price_range and price_range in price_ranges:
            min_price, max_price = price_ranges[price_range]
            books = books.filter(price__price__gte=min_price, price__price__lte=max_price)

        genres = Genre.objects.all()
        categories = Categories.objects.all()

        context = {
            "books": books,
            "genres": genres,
            "categories": categories,
            "price_ranges": price_ranges,
            "selected_price_range": price_range
        }

        return render(request, 'base/books.html', context)
    else:
        return render(request, 'base/about.html')

@login_required(login_url='login')
def cart(request, pk):
    search = request.GET.get("search") if request.GET.get('search') != None else ''
    total_price=0
    if search:
        price_range = request.GET.get("price_range", None)

        price_ranges = {
            "0-10": (0, 10),
            "10-15": (10, 15),
            "15-20": (15, 20),
            "20-25": (20, 25),
            "25-50": (25, 50),
        }

        books = Book.objects.filter(
            Q(name__icontains=search) | Q(author__name__icontains=search) | Q(genre__name__icontains=search) | Q(categories__name__icontains=search)).distinct()

        if price_range and price_range in price_ranges:
            min_price, max_price = price_ranges[price_range]
            books = books.filter(price__price__gte=min_price, price__price__lte=max_price)

        genres = Genre.objects.all()
        categories = Categories.objects.all()

        context = {
            "books": books,
            "genres": genres,
            "categories": categories,
            "price_ranges": price_ranges,
            "selected_price_range": price_range
        }

        return render(request, 'base/books.html', context)
    else:
        user= User.objects.get(id=pk)
        books = user.books.all()
        for book in books:
            total_price+=book.price.price

        context = {"books": books, 'total_price': total_price}
        return render(request, 'base/cart.html', context)

@login_required(login_url='login')
def adding(request, id):
    user=request.user
    book=Book.objects.get(id=id)
    user.books.add(book)
    return redirect('cart', request.user.id)


@login_required(login_url='login')
def delete(request, id):
    obj = Book.objects.get(id=id)
    if request.method=="POST":
        request.user.books.remove(obj)
        return redirect('cart', request.user.id)

    return render(request, 'base/delete.html', {'obj': obj} )

@login_required(login_url='login')
def drop(request, id):
    book =Book.objects.get(id=id)
    if request.method=='POST':
        book.picture.delete()
        book.delete()
        return redirect('home')
    return render(request, 'base/delete.html', {'book': book })

def login_user(request):
    if request.user.is_authenticated:
        return redirect('cart', request.user.id)
    if request.method == 'POST':
        username=request.POST.get('username').lower()
        password=request.POST.get('password')

        try:
            user=User.objects.get(username=username)
        except:
            messages.error(request, 'User does not exist!')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('profile', request.user.id)
        else:
            messages.error(request, 'User or Password is not exist!')
    return render(request, 'base/login.html')

def logout_user(request):
    logout(request)
    return redirect('home')


def registration(request):
    form=MyUserCreationForm()
    if request.method == 'POST':
        form = MyUserCreationForm(request.POST)
        if form.is_valid():
            user=form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            login(request, user)
            return redirect('profile', user.id)
        else:
            messages.error(request, 'Follow the instructions and create proper user and password')
    context = {'form': form}
    return render(request, 'base/registration.html', context)

@login_required(login_url='login')
def add_book(request):
    search = request.GET.get("search") if request.GET.get('search') else ''
    if search:
        price_range = request.GET.get("price_range", None)

        price_ranges = {
            "0-10": (0, 10),
            "10-15": (10, 15),
            "15-20": (15, 20),
            "20-25": (20, 25),
            "25-50": (25, 50),
        }

        books = Book.objects.filter(
            Q(name__icontains=search) |
            Q(author__name__icontains=search) |
            Q(genre__name__icontains=search) |
            Q(categories__name__icontains=search)
        ).distinct()

        if price_range and price_range in price_ranges:
            min_price, max_price = price_ranges[price_range]
            books = books.filter(price__price__gte=min_price, price__price__lte=max_price)

        genres = Genre.objects.all()
        categories = Categories.objects.all()

        context = {
            "books": books,
            "genres": genres,
            "categories": categories,
            "price_ranges": price_ranges,
            "selected_price_range": price_range
        }

        return render(request, 'base/books.html', context)
    else:
        authors = Author.objects.all()
        genres = Genre.objects.all()
        form = BookForm()

        if request.method == 'POST':
            book_author = request.POST.get('author')
            book_genre = request.POST.get('genre')
            book_price_id = request.POST.get('price')

            author, created = Author.objects.get_or_create(name=book_author)
            genre, created = Genre.objects.get_or_create(name=book_genre)


            price = get_object_or_404(Price, pk=int(book_price_id))

            form = BookForm(request.POST)

            new_book = Book(
                picture=request.FILES.get('picture'),
                name=form.data['name'],
                author=author,
                description=form.data['description'],
                price=price,  # Assign the Price instance
                creator=request.user
            )

            if not Book.objects.filter(picture=request.FILES.get('picture')).exists():
                new_book.save()
                new_book.genre.add(genre)
            else:
                messages.error(request, 'Book with the same picture already exists...')

            return redirect('books')

        context = {'form': form, 'authors': authors, 'genres': genres}
        return render(request, 'base/add_book.html', context)


def book(request, id):
    search = request.GET.get("search") if request.GET.get('search') != None else ''
    if search:
        price_range = request.GET.get("price_range", None)

        price_ranges = {
            "0-10": (0, 10),
            "10-15": (10, 15),
            "15-20": (15, 20),
            "20-25": (20, 25),
            "25-50": (25, 50),
        }

        books = Book.objects.filter(
            Q(name__icontains=search) | Q(author__name__icontains=search) | Q(genre__name__icontains=search) | Q(categories__name__icontains=search)).distinct()

        if price_range and price_range in price_ranges:
            min_price, max_price = price_ranges[price_range]
            books = books.filter(price__price__gte=min_price, price__price__lte=max_price)

        genres = Genre.objects.all()
        categories = Categories.objects.all()

        context = {
            "books": books,
            "genres": genres,
            "categories": categories,
            "price_ranges": price_ranges,
            "selected_price_range": price_range
        }

        return render(request, 'base/books.html', context)
    else:
        book = Book.objects.get(id=id)
        book_comments=book.comment_set.all()
        author=Author.objects.get(name=book.author)
        if request.method == "POST":
            Comment.objects.create(
                user = request.user,
                book=book,
                body=request.POST.get('body')
            )
        return  render(request, 'base/book.html', {'book': book, 'author': author, 'comments': book_comments})

def author(request, id):
    search = request.GET.get("search") if request.GET.get('search') != None else ''
    if search:
        price_range = request.GET.get("price_range", None)

        price_ranges = {
            "0-10": (0, 10),
            "10-15": (10, 15),
            "15-20": (15, 20),
            "20-25": (20, 25),
            "25-50": (25, 50),
        }

        books = Book.objects.filter(
            Q(name__icontains=search) | Q(author__name__icontains=search) | Q(genre__name__icontains=search) | Q(categories__name__icontains=search)).distinct()

        if price_range and price_range in price_ranges:
            min_price, max_price = price_ranges[price_range]
            books = books.filter(price__price__gte=min_price, price__price__lte=max_price)

        genres = Genre.objects.all()
        categories = Categories.objects.all()

        context = {
            "books": books,
            "genres": genres,
            "categories": categories,
            "price_ranges": price_ranges,
            "selected_price_range": price_range
        }

        return render(request, 'base/books.html', context)
    else:
        author = Author.objects.get(id=id)
        books=Book.objects.filter(author=author)
        return render(request, 'base/author.html', {'author': author, 'books':books})

def serie(request, id):
    search = request.GET.get("search") if request.GET.get('search') != None else ''
    if search:
        price_range = request.GET.get("price_range", None)

        price_ranges = {
            "0-10": (0, 10),
            "10-15": (10, 15),
            "15-20": (15, 20),
            "20-25": (20, 25),
            "25-50": (25, 50),
        }

        books = Book.objects.filter(
            Q(name__icontains=search) | Q(author__name__icontains=search) | Q(genre__name__icontains=search) | Q(categories__name__icontains=search)).distinct()

        if price_range and price_range in price_ranges:
            min_price, max_price = price_ranges[price_range]
            books = books.filter(price__price__gte=min_price, price__price__lte=max_price)

        genres = Genre.objects.all()
        categories = Categories.objects.all()

        context = {
            "books": books,
            "genres": genres,
            "categories": categories,
            "price_ranges": price_ranges,
            "selected_price_range": price_range
        }

        return render(request, 'base/books.html', context)
    else:
        serie=Series.objects.get(id=id)
        context={'serie':serie, 'author': author}
        return render(request, 'base/serie.html', context)

@login_required(login_url='login')
def update_user(request):
    search = request.GET.get("search") if request.GET.get('search') != None else ''
    if search:
        price_range = request.GET.get("price_range", None)

        price_ranges = {
            "0-10": (0, 10),
            "10-15": (10, 15),
            "15-20": (15, 20),
            "20-25": (20, 25),
            "25-50": (25, 50),
        }

        books = Book.objects.filter(
            Q(name__icontains=search) | Q(author__name__icontains=search) | Q(genre__name__icontains=search) | Q(categories__name__icontains=search)).distinct()

        if price_range and price_range in price_ranges:
            min_price, max_price = price_ranges[price_range]
            books = books.filter(price__price__gte=min_price, price__price__lte=max_price)

        genres = Genre.objects.all()
        categories = Categories.objects.all()

        context = {
            "books": books,
            "genres": genres,
            "categories": categories,
            "price_ranges": price_ranges,
            "selected_price_range": price_range
        }

        return render(request, 'base/books.html', context)
    else:
        user=request.user
        form=UserForm(instance=user)
        if request.method == 'POST':
            form=UserForm(request.POST, request.FILES, instance=user)
            if form.is_valid():
                form.save()
                return redirect('profile', user.id)


        context = {'form': form}
        return render(request, 'base/update_user.html', context)





@login_required(login_url='login')
def delete_comment(request, id):
    comment = Comment.objects.get(id=id)
    book=comment.book
    if request.method=='POST':
        comment.delete()
        return redirect('book', book.id)
    return render(request, 'base/delete.html', {'obj' : comment} )

@login_required(login_url='login')
def profile(request, id):
    search = request.GET.get("search") if request.GET.get('search') != None else ''
    if search:
        price_range = request.GET.get("price_range", None)

        price_ranges = {
            "0-10": (0, 10),
            "10-15": (10, 15),
            "15-20": (15, 20),
            "20-25": (20, 25),
            "25-50": (25, 50),
        }

        books = Book.objects.filter(
            Q(name__icontains=search) | Q(author__name__icontains=search) | Q(genre__name__icontains=search) | Q(categories__name__icontains=search)).distinct()

        if price_range and price_range in price_ranges:
            min_price, max_price = price_ranges[price_range]
            books = books.filter(price__price__gte=min_price, price__price__lte=max_price)

        genres = Genre.objects.all()
        categories = Categories.objects.all()

        context = {
            "books": books,
            "genres": genres,
            "categories": categories,
            "price_ranges": price_ranges,
            "selected_price_range": price_range
        }

        return render(request, 'base/books.html', context)
    else:
        user=User.objects.get(id=id)
        books=Book.objects.filter(creator=user)
        context={'user': user, 'books':books}
        return render(request, 'base/profile.html', context)



def edit_book(request, id):
    search = request.GET.get("search") if request.GET.get('search') != None else ''
    if search:
        price_range = request.GET.get("price_range", None)

        price_ranges = {
            "0-10": (0, 10),
            "10-15": (10, 15),
            "15-20": (15, 20),
            "20-25": (20, 25),
            "25-50": (25, 50),
        }

        books = Book.objects.filter(
            Q(name__icontains=search) | Q(author__name__icontains=search) | Q(genre__name__icontains=search) | Q(categories__name__icontains=search)).distinct()

        if price_range and price_range in price_ranges:
            min_price, max_price = price_ranges[price_range]
            books = books.filter(price__price__gte=min_price, price__price__lte=max_price)

        genres = Genre.objects.all()
        categories = Categories.objects.all()

        context = {
            "books": books,
            "genres": genres,
            "categories": categories,
            "price_ranges": price_ranges,
            "selected_price_range": price_range
        }

        return render(request, 'base/books.html', context)
    else:
        user=request.user
        book=Book.objects.get(id=id)
        form = BookForm(instance=book)
        if request.method == 'POST':
            form=BookForm(request.POST, request.FILES, instance=book)
            if form.is_valid():
                form.save()
                return redirect('profile', user.id)


        context={'book': book, 'form':form}

    return render(request, 'base/edit_book.html', context)

