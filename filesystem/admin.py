from django.contrib import admin

from filesystem.models import Project, Directory, File

admin.site.register(Project)
admin.site.register(Directory)
admin.site.register(File)

