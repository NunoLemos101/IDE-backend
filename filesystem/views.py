from django.shortcuts import render
from filesystem.models import Project, File


def format_html_file(project):
    index_file = File.objects.get(name="index.html", project=project)
    temp = index_file.code
    for file in project.file_set.all():
        file_code = file.code
        # INCLUDE(/test/src/components/card.js)
        if f'#INCLUDE({file.__str__()})' in temp:
            temp = temp.replace(f'#INCLUDE({file.__str__()})', f'<script>{file.code}</script>')
    return temp


def index(request):
    project = Project.objects.get(path=request.path)
    project.generate_build(project.file_set.get(name="index.html"))
    return render(request, "filesystem/index.html", {'html_file': project.build})
