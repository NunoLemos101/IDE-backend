from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Project(models.Model):

    path = models.CharField(max_length=256, blank=False)

    def __str__(self):
        return self.path


class Directory(models.Model):

    project = models.ForeignKey(Project, on_delete=models.CASCADE, null=False, blank=False)
    parent_directory = models.ForeignKey('Directory', on_delete=models.CASCADE, null=True, blank=True)
    node = models.PositiveIntegerField(default=0)
    name = models.TextField()

    def __str__(self):
        folder_name = self.name
        path = [folder_name + '/', ]
        string = 'self.parent_directory'
        while eval(string) is not None:
            path.append(eval(string).name + '/')
            string = string + '.parent_directory'
        return self.project.__str__() + ''.join(reversed(path))


class File(models.Model):

    name = models.TextField()
    code = models.TextField()
    project = models.ForeignKey(Project, on_delete=models.CASCADE, null=False, blank=False)
    directory = models.ForeignKey(Directory, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        if self.directory:
            return '{}{}'.format(self.directory.__str__(), self.name)
        return '{}{}'.format(self.project.path, self.name)