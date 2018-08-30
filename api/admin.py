from django.contrib import admin

from .models import Notebook, Note


admin.site.site_header = 'HamsterDemo administration'
admin.site.site_title = 'HamsterDemo site admin'

admin.site.register(Notebook)
admin.site.register(Note)
