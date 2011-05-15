from django.contrib import admin
from models import Entry


class EntryAdmin(admin.ModelAdmin):
    list_display = ('name', 'cpf', 'poster_presentation')
    list_filter = ('poster_presentation','people_type','institution')

admin.site.register(Entry, EntryAdmin)
