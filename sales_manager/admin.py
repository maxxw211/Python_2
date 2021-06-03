from django.contrib import admin
from sales_manager.models import Book, Comment


class CommentAdmin(admin.StackedInline):
    model = Comment


class BookInLine(admin.ModelAdmin):
    inlines = (CommentAdmin,)
    list_filter = ('date_publish',)
    list_editable = ('text',)
    list_display = ('title', 'text',)


admin.site.register(Book, BookInLine)
