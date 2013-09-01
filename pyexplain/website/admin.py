from django.contrib import admin
from .models import Keyword, Category

class KeywordAdmin(admin.ModelAdmin):
    list_display = ('codname', 'category')
    list_filter = ('category',)

admin.site.register(Keyword, KeywordAdmin)
admin.site.register(Category)