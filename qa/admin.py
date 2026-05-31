
"""Admin configuration for Q&A platform."""

from django.contrib import admin
from .models import UserProfile, Question


@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'location', 'created_at']
    search_fields = ['user__username']


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ['user', 'short_question', 'created_at']
    search_fields = ['user__username', 'question']

    def short_question(self, obj):
        return obj.question[:60]
    short_question.short_description = 'Question'