from django.contrib import admin
from .models import Message


class MessageAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'timestamp', 'message_id']

    class Meta:
        model = Message


admin.site.register(Message, MessageAdmin)
