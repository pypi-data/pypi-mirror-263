from django.contrib import admin

from .models import BlackList


@admin.register(BlackList)
class BlackListAdmin(admin.ModelAdmin):
    list_display = ('created', 'user_id', 'comment')
    search_fields = ('=user_id',)
    ordering = ('-created', )
