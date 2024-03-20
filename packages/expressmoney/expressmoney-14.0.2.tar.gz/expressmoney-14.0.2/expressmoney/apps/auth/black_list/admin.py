from django.contrib import admin

from black_list import models


@admin.register(models.BlackList)
class BlackListAdmin(admin.ModelAdmin):
    list_display = ('created', 'user', 'comment')
    search_fields = ('=user_id',)
    ordering = ('-created', )

    def has_change_permission(self, request, obj=None):
        return False
