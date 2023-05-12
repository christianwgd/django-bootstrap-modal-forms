from django.contrib import admin

from examples.models import Book, Reader


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ['title', 'author']


@admin.register(Reader)
class ReaderAdmin(admin.ModelAdmin):
    list_display = ['name']