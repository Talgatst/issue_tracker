from django.contrib import admin
from webapp.models import Status, Type, Issue


@admin.register(Status)
class StatusAdmin(admin.ModelAdmin):
    pass


@admin.register(Type)
class TypeAdmin(admin.ModelAdmin):
    pass


@admin.register(Issue)
class IssueAdmin(admin.ModelAdmin):
    pass

