from django.contrib import admin
from models import Tag, ToDoItem


class TagAdmin(admin.ModelAdmin):
    """Defines customizations for the admin site"""
    search_fields = ("name",)


class ToDoItemAdmin(admin.ModelAdmin):
    """Defines customizations for the admin site"""
    search_fields = ("name", "creator__username")
    filter_horizontal = ("interests", "tags", "users_claimed", "sub_tasks")
    list_display = ("name", "due", "status", "importance", "excellence", "creator", "creation_date")
    list_filter = ("due", "status", "importance", "creation_date")
    date_hierarchy = "creation_date"
    fieldsets = (
        (None, {
            "fields": (("name", "status"), ("creator", "completed_by"), "details", "excellence", ("importance", "due"), "sub_tasks")
        }),
        ("Meta-data", {
            "classes": ("collapse",),
            "fields": ("interests", "tags")
        }),
        ("Claims", {
            "classes": ("collapse",),
            "fields": ("users_claimed",)
        })
    )

admin.site.register(Tag, TagAdmin)
admin.site.register(ToDoItem, ToDoItemAdmin)
