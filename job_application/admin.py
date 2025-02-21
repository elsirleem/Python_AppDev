from django.contrib import admin
from .models import Form

# Register your models here.
class FormAdmin(admin.ModelAdmin):
    list_display = ["firstname", "lastname", "email", "date", "occupation"]
    search_fields = ["firstname", "lastname", "email", "date", "occupation"]
    list_filter = ["date"]
    readonly_fields = ["date"]

admin.site.register(Form, FormAdmin)