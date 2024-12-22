from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.forms import UserCreationForm
from django.core.paginator import Paginator
from django.http import JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from .models import Book, Category


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

    if category_id:
        category = get_object_or_404(Category, id=category_id)
        books = books.filter(category=category)

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
@user_passes_test(lambda u: u.is_superuser, login_url='admin')
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





def feedback(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        feedback_text = request.POST.get('feedback')

        if name and email and feedback_text:
            # Process the feedback (e.g., save to the database)
            # Return JSON response with success message and redirect URL
            return JsonResponse({'success': True, 'message': 'Thank you for your feedback!', 'redirect_url': '/feedback_confirmation/'})
        else:
            return JsonResponse({'success': False, 'message': 'All fields are required.'})
    return render(request, 'feedback.html')



def registration(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            return JsonResponse({'success': True, 'message': f'Account created for {username}.', 'redirect_url': '/registration_confirmation/'})
        else:
            errors = form.errors.as_json()
            return JsonResponse({'success': False, 'message': 'Something went wrong. Please try again.', 'errors': errors})
    else:
        form = UserCreationForm()
    return render(request, 'registration.html', {'form': form})

def registration_confirmation(request):
    return render(request, 'registration_confirmation.html')




def studentlogin(request):
    form = AuthenticationForm(request, data=request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            login(request, form.get_user())
            return JsonResponse({'success': True, 'redirect_url': '/index/'})  # JSON response for success
        else:
            errors = form.errors.as_json()
            return JsonResponse({'success': False, 'message': 'Invalid login credentials. Please try again.', 'errors': errors})  # JSON response for errors
    return render(request, 'studentlogin.html', {'form': form})



def logout_view(request):
    logout(request)
    messages.success(request, "You have successfully logged out.")
    return redirect('index')


def feedback_confirmation(request):
    return render(request, 'feedback_confirmation.html')


@login_required
def return_confirmation(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    return render(request, 'return_confirmation.html', {'book': book})
