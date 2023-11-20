from django.contrib import admin
from usersapp.models import User


@admin.register(User)
class UsersAdmin(admin.ModelAdmin):
    list_display = ('pk', 'email', 'country', 'email_verify',)
    list_filter = ('email',)
    search_fields = ('email',)
