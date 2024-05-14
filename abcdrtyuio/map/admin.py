from django.contrib import admin

from.models import Heh
from.models import Category

class HehAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'data', 'photo')
    list_display_links = ('id', 'title')
    search_fields = ('title', 'content')
    list_filter = ('data',)
    
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')
    search_fields = ('name',)

admin.site.register(Heh, HehAdmin)
admin.site.register(Category, CategoryAdmin)
