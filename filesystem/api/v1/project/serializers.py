from rest_framework import serializers

from filesystem.models import File, Directory, Project


class FileSerializer(serializers.ModelSerializer):

    class Meta:
        model = File
        fields = '__all__'


class DirectorySerializer(serializers.ModelSerializer):

    directories = serializers.SerializerMethodField(read_only=True)
    files = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Directory
        fields = ['id', 'node', 'name', 'project', 'directories', 'files']

    def get_directories(self, directory):
        return DirectorySerializer(Directory.objects.filter(parent_directory=directory), many=True).data

    def get_files(self, folder):
        return FileSerializer(folder.file_set.all(), many=True).data


class FileSystemSerializer(serializers.ModelSerializer):

    directories = serializers.SerializerMethodField(read_only=True)
    files = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Project
        fields = ['id', 'path', 'directories', 'files']

    def get_directories(self, project):
        return DirectorySerializer(project.directory_set.filter(node=0), many=True).data

    def get_files(self, project):
        return FileSerializer(project.file_set.filter(directory__isnull=True), many=True).data