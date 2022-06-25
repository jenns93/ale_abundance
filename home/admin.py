from django.contrib import admin

# Register your models here.
from .models import Contact




class ContactAdmin(admin.ModelAdmin):
    list_display = (
        'full_name',
        'email',
        'issue_type',
        'issue_details'
    )


admin.site.register(Contact, ContactAdmin)
