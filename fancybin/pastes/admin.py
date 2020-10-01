from django.contrib import admin

from pastes.models import Paste

# Register your models here.

class PasteAdmin(admin.ModelAdmin):
  pass
admin.site.register(Paste, PasteAdmin)
