from django.contrib import admin
from .models import ChatThread, Message


@admin.register(ChatThread)
class ChatThreadAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "user",
        "title",
        "created_at",
        "updated_at",
    )


@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "thread",
        "role",
        "created_at",
    )