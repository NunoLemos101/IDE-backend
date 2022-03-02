from rest_framework.response import Response
from rest_framework.viewsets import ViewSet

from filesystem.api.v1.project.serializers import FileSystemSerializer
from filesystem.models import File, Directory, Project


class ProjectViewSet(ViewSet):

    def retrieve(self, request, pk, *args, **kwargs):
        return Response(data=FileSystemSerializer(Project.objects.get(pk=pk)).data, status=200)

