from django.http import HttpResponse
from rest_framework.viewsets import ViewSet

from filesystem.models import File, Directory, Project


class FileViewSet(ViewSet):

    def create(self, request, *args, **kwargs):

        project = Project.objects.get(pk=request.data['project_id'])

        # Meaning It's created in root and there is no files with same name
        if request.data['directory_id'] is None and File.objects.filter(directory__isnull=True, project=project).count() == 0:
            File.objects.create(name=request.data['name'], code="// {}".format(request.data['name']), project=project)
            return HttpResponse(status=201)

        directory = Directory.objects.get(pk=request.data['directory_id'])
        if File.objects.filter(directory=directory).count() == 0:
            File.objects.create(name=request.data['name'], code="// {}".format(request.data['name']), directory=directory, project=project)
        return HttpResponse(status=201)

    def save(self, request, pk, *args, **kwargs):
        file = File.objects.get(pk=request.data['fileId'])
        file.code = request.data['code']
        file.save()
        return HttpResponse(status=200)
