from rest_framework.response import Response
from rest_framework.viewsets import ViewSet

from filesystem.api.v1.project.serializers import FileSystemSerializer
from filesystem.models import Project, File


class ProjectViewSet(ViewSet):

    def retrieve(self, request, pk, *args, **kwargs):
        return Response(data=FileSystemSerializer(Project.objects.get(pk=pk)).data, status=200)

    def build(self, request, pk, *args, **kwargs):
        project = Project.objects.get(pk=pk)
        index_file = File.objects.get(pk=request.data['index_file_id'], project=project)
        project.generate_build(index_file)
        return Response(data={"message": "SUCCESS"}, status=200)
