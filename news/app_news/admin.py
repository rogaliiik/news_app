from django.contrib import admin
from app_news.models import *


class CommentaryInline(admin.TabularInline):
    model = Commentary


@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'is_active', 'created_at', 'updated_at']
    list_filter = ['is_active', 'created_at']
    inlines = [CommentaryInline]
    search_fields = ['title', 'description']

    actions = ['active', 'non_active']

    def active(self, request, query):
        query.update(is_active=True)

    def non_active(self, request, query):
        query.update(is_active=False)

    active.short_description = 'Активно'
    non_active.short_description = 'Неактивно'


@admin.register(Commentary)
class CommentaryAdmin(admin.ModelAdmin):
    list_display = ['id', 'status' , 'news', 'description', 'user_name', "user"]
    list_filter = ['user_name']
    search_fields = ['user_name', 'description']
    fieldsets = (
        ('Сведения о пользователе', {
            'fields':('user_name',),
            'description': 'Различные данные об авторе'
        }),
        ('Комментарий',{
            'fields':('news', 'description'),
            'description': 'Информация о комментарии'
        })
    )

    actions = ['delete_by_admin']

    def delete_by_admin(self, request, queryset):
        queryset.update(status='d', description='Удалено администратором')

    delete_by_admin.short_description = 'Удалено администратором'

