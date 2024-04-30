from django.contrib import admin

from feedback.models import Feedback


@admin.register(Feedback)
class FeedbackAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'comment', 'phone_number')
    list_display_links = ('email',)
