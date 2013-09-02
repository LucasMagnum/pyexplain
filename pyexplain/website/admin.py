from django.contrib import admin
from .models import Keyword, Category


class KeywordAdmin(admin.ModelAdmin):
    list_display = ('codname', 'category', 'description')
    list_filter = ('category',)
    search_fields = ('category__name',)


admin.site.register(Keyword, KeywordAdmin)
admin.site.register(Category)