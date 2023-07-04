from django.contrib import admin
from book_models_view.models import Books

# Register your models here.

class HomeAdmin(admin.ModelAdmin):
    list_display = ('name', 'author', 'info')
    list_display_links = ('name', 'author')
    ordering = ('author',)
admin.site.register(Books, HomeAdmin)

