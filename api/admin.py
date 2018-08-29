from django.contrib import admin

from .models import Notebook, Note


class NotebookAdmin(admin.ModelAdmin):
    pass

class NoteAdmin(admin.ModelAdmin):
    pass


admin.site.register(Notebook, admin.ModelAdmin)
admin.site.register(Note, NoteAdmin)
