from django.contrib import admin
from models import Update, Comment, Tag, ToDoItem


class TagAdmin(admin.ModelAdmin):
    """Defines customizations for the admin site"""
    search_fields = ("name",)


class ToDoItemAdmin(admin.ModelAdmin):
    """Defines customizations for the admin site"""
    search_fields = ("name", "creator__username")
    filter_horizontal = ("interests", "tags", "users_claimed", "sub_tasks")
    list_display = ("name", "due", "completed", "importance", "excellence", "creator", "creation_date")
    list_filter = ("due", "completed", "importance", "creation_date")
    date_hierarchy = "creation_date"
    fieldsets = (
        (None, {
            "fields": (("name", "completed"), ("creator", "completed_by"), "details", "excellence", ("importance", "due"), "sub_tasks")
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


class UpdateAdmin(admin.ModelAdmin):
    """Defines customizations for the admin site"""
    search_fields = ("title", "user__username")
    list_display = ("title", "date", "user", "todoitem")
    list_filter = ("date",)
    date_hierarchy = "date"
    raw_id_fields = ("todoitem",)
    ordering = ("-date",)


class CommentAdmin(admin.ModelAdmin):
    """Defines customizations for the admin site"""
    search_fields = ("title", "user__username")
    list_display = ("title", "date", "user", "todoitem")
    list_filter = ("date",)
    date_hierarchy = "date"
    raw_id_fields = ("todoitem",)
    ordering = ("-date",)

admin.site.register(Update, UpdateAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(Tag, TagAdmin)
admin.site.register(ToDoItem, ToDoItemAdmin)
