from django.contrib import admin
from mock_server.models import Response


@admin.register(Response)
class CategoryListAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "content",
        "created_at",
    )
