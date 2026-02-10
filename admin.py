from django.contrib import admin

from .models import JobApplication


@admin.register(JobApplication)
class JobApplicationAdmin(admin.ModelAdmin):
    list_display = ("student", "job", "status", "applied_at")
    list_filter = ("status", "job__company")
    search_fields = ("student__full_name", "job__title")
