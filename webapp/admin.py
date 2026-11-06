from django.contrib import admin
from webapp.models import Todo, Status, Type

@admin.register(Status)
class StatusAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')


@admin.register(Type)
class TypeAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')


@admin.register(Todo)
class TodoAdmin(admin.ModelAdmin):
    list_display = ('id', 'summary', 'status', 'type', 'created_at')
    list_filter = ('status', 'type')
    search_fields = ('summary', 'description')