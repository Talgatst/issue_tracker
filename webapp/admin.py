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
    list_display = ('summary', 'description', 'status', 'display_types', 'created_at', 'updated_at')
    list_filter = ('status', 'types__name')
    search_fields = ('description',)

    filter_horizontal = ('types',)

    def display_types(self, obj):
        return ", ".join([type.name for type in obj.types.all()])
    display_types.short_description = 'Типы'



