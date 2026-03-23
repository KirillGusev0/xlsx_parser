from django.contrib import admin
from parser.models import EmailTask

# Register your models here.


@admin.register(EmailTask)
class EmailTaskAdmin(admin.ModelAdmin):

    list_display = (
        "id",
        "external_id",
        "email",
        "status",
        "created_at",
    )

    list_display_links = (
        "id",
        "external_id",
    )

    list_filter = (
        "status",
        "created_at",
    )

    search_fields = (
        "external_id",
        "email",
    )

    ordering = ("-created_at",)
