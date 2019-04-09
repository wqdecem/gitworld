from django.contrib import admin

from .models import Scan



class ScanAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['scan_text']}),

    ]


admin.site.register(Scan, ScanAdmin)
