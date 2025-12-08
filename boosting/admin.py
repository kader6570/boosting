from django.contrib import admin
from .models import Inscription

# Register your models here.
class AdminInscription(admin.ModelAdmin):
    list_display = ('tiktok_username','numero')

admin.site.register(Inscription,AdminInscription)