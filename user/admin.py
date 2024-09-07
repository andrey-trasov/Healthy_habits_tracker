from django.contrib import admin

from user.models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = (
        "email",
        "phone_number",
        "avatar",
        "token",
        "city",
        "telegram_chat_id",
    )
