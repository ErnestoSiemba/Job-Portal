from django.contrib import admin
from .models import Job, Applicant

admin.site.register(Applicant)

@admin.register(Job)
class JobAdmin(admin.ModelAdmin):
    search_fields = ['title', 'company_name']
    list_display = ['title', 'company_name', 'location', 'salary', 'location']
    list_per_page = 10
    ordering = ['title']