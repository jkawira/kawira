from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('admin/', views.admin, name='admin'),
    path('book/', views.book, name='book'),
    path('feedback/', views.feedback, name='feedback'),
    path('registration/', views.registration, name='registration'),
    path('studentlogin/', views.studentlogin, name='studentlogin'),
    path('feedback_confirmation/', views.feedback_confirmation, name='feedback_confirmation'),
    path('registration_confirmation/', views.registration_confirmation, name='registration_confirmation'),
    path('logout/', views.logout_view, name='logout'),
    path('borrow/<int:book_id>/', views.borrow_book, name='borrow_book'),
    path('borrow_confirmation/<int:book_id>/', views.borrow_confirmation, name='borrow_confirmation'),
    path('return/<int:book_id>/', views.return_book, name='return_book'),
    path('return_confirmation/<int:book_id>/', views.return_confirmation, name='return_confirmation'),
    path('admin_borrowed_books/', views.admin_borrowed_books, name='admin_borrowed_books'),
]
