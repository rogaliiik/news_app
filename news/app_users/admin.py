from django.contrib import admin
from app_users.models import Profile


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'city', 'date_of_birth']

