from django.contrib import admin

from blogapp.models import Blog


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('header', 'slug', 'picture', 'public_sign',)
    # list_filter = ('category',)
    # search_fields = ('name', 'description',)
