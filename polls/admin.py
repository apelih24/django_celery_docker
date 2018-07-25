from django.contrib import admin
from .models import IcoList


# Register your models here.

class IcoListAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name', 'ico_scale', 'total')
    search_fields = ['name']


admin.site.register(IcoList, IcoListAdmin)
