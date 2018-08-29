from django.contrib import admin

from .models import Notebook, Note


admin.site.site_header = 'HamsterDemo administration'
admin.site.site_title = 'HamsterDemo site admin'


class NotebookAdmin(admin.ModelAdmin):
    pass


class NoteAdmin(admin.ModelAdmin):
    pass


admin.site.register(Notebook, admin.ModelAdmin)
admin.site.register(Note, NoteAdmin)
