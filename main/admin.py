from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, Tag, Task

admin.site.register(User, UserAdmin)


class TaskManagerAdminSite(admin.AdminSite):
    pass


task_manager_admin_site = TaskManagerAdminSite(name="Task manager admin")


@admin.register(Tag, site=task_manager_admin_site)
class TagAdmin(admin.ModelAdmin):
    list_display = ("title", "identifier")


@admin.register(Task, site=task_manager_admin_site)
class TaskAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "description",
        "author",
        "assigned",
        "priority",
        "due_date",
        "state",
    )
    list_editable = ("due_date", "state", "priority", "assigned")

    ordering = ("due_date",)


class SuperAdmin(UserAdmin):
    model = User
    add_fieldsets = (*UserAdmin.add_fieldsets, ("New fields", {"fields": ("role",)}))
    fieldsets = (*UserAdmin.fieldsets, ("New field", {"fields": ("role",)}))
    list_display = ("username", "last_name", "first_name", "role", "email")
    list_editable = ("role",)


task_manager_admin_site.register(User, SuperAdmin)
