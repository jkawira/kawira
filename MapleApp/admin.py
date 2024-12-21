from django.contrib import admin
from .models import Admin, Book, Feedback, Student, Category

class AdminAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
    search_fields = ('name',)

class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'category', 'description')
    search_fields = ('title', 'author')
    list_filter = ('author', 'category')
    ordering = ('title',)

class FeedbackAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'message')
    search_fields = ('name', 'email')
    ordering = ('name',)

class StudentAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'username', 'email')
    search_fields = ('username', 'email')
    list_filter = ('books',)
    ordering = ('username',)

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
    search_fields = ('name',)
    ordering = ('name',)

admin.site.register(Admin, AdminAdmin)
admin.site.register(Book, BookAdmin)
admin.site.register(Feedback, FeedbackAdmin)
admin.site.register(Student, StudentAdmin)
admin.site.register(Category, CategoryAdmin)
