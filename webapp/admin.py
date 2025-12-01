from django.contrib import admin
from webapp.models import Status, Type, Issue


@admin.register(Status)
class StatusAdmin(admin.ModelAdmin):
    list_display = ('name',)
    list_filter = ('id', 'name')
    search_fields = ('name',)


@admin.register(Type)
class TypeAdmin(admin.ModelAdmin):
    list_display = ('name',)
    list_filter = ('id', 'name')
    search_fields = ('name',)


@admin.register(Issue)
class IssueAdmin(admin.ModelAdmin):
    list_display = ('summary', 'description', 'status', 'type', 'created_at', 'updated_at')
    list_filter = ('status', 'type')
    search_fields = ('description',)


