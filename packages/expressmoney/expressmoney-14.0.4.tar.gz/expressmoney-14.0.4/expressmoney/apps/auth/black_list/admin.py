from django.contrib import admin

from .models import BlackList


@admin.register(BlackList)
class BlackListAdmin(admin.ModelAdmin):
    list_display = ('created', 'user', 'comment')
    search_fields = ('=user_id',)
    ordering = ('-created', )

    def has_change_permission(self, request, obj=None):
        return False
