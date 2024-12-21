from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from django.shortcuts import render, redirect, get_object_or_404
from django.core.paginator import Paginator
from .models import Book, Category
from django.contrib.auth.decorators import login_required, user_passes_test  # Add this import

def index(request):
    return render(request, 'index.html')

def admin(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, f"Welcome, {user.username}!")
                return redirect('index')
            else:
                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Invalid credentials, please try again.")
    else:
        form = AuthenticationForm()
    return render(request, 'admin.html', {'form': form})


def book(request):
    query = request.GET.get('q')
    category_id = request.GET.get('category')

    books = Book.objects.all()

    if query:
        books = books.filter(title__icontains=query)
        print(f"Books found with query '{query}': {books}")

    if category_id:
        books = books.filter(category_id=category_id)
        print(f"Books found in category '{category_id}': {books}")

    categories = Category.objects.all()
    paginator = Paginator(books, 10)  # Show 10 books per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'book.html', {
        'page_obj': page_obj,
        'categories': categories,
        'selected_category': category_id,
        'query': query,
    })

@login_required
def borrow_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    if book.borrowed:
        messages.error(request, "This book is already borrowed.")
    else:
        book.borrowed = True
        book.borrowed_by = request.user
        book.save()
        messages.success(request, f"You have successfully borrowed '{book.title}'")
    return redirect('borrow_confirmation', book_id=book.id)

@login_required
@user_passes_test(lambda u: u.is_superuser)
def admin_borrowed_books(request):
    books = Book.objects.filter(borrowed=True)
    return render(request, 'admin_borrowed_books.html', {'books': books})

@login_required
def return_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    if not book.borrowed:
        messages.error(request, "This book is already available.")
    else:
        book.borrowed = False
        book.borrowed_by = None  # Clear the borrowed_by field
        book.save()
        messages.success(request, f"You have successfully returned '{book.title}'")
    return redirect('return_confirmation', book_id=book.id)

@login_required
def borrow_confirmation(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    return render(request, 'borrow_confirmation.html', {'book': book})

from django.shortcuts import render, redirect

def feedback(request):
    if request.method == 'POST':
        feedback_text = request.POST.get('feedback')
        return redirect('feedback_confirmation')
    return render(request, 'feedback.html')

def registration(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']
        if password != confirm_password:
            messages.error(request, "Passwords do not match.")
            return render(request, 'registration.html', {'error_message': "Passwords do not match."})
        if User.objects.filter(email=email).exists():
            messages.error(request, "Email is already registered.")
            return render(request, 'registration.html', {'error_message': "Email is already registered."})
        user = User.objects.create_user(username=email, email=email, password=password)
        user.save()
        messages.success(request, "Account created successfully. Please log in.")
        return redirect('registration_confirmation')
    return render(request, 'registration.html')

def studentlogin(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            messages.error(request, "Invalid username or password.")
    return render(request, 'studentlogin.html')

def registration_confirmation(request):
    return render(request, 'registration_confirmation.html')

def logout_view(request):
    logout(request)
    return redirect('index')

def feedback_confirmation(request):
    return render(request, 'feedback_confirmation.html')

@login_required
def return_confirmation(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    return render(request, 'return_confirmation.html', {'book': book})



def logout_view(request):
    logout(request)
    messages.success(request, "You have successfully logged out.")
    return redirect('index')
