from django.urls import path, include

from filesystem.api.v1.project.router import ProjectRouter
from filesystem.api.v1.project.views import ProjectViewSet
from filesystem.api.v1.file.router import FileRouter
from filesystem.api.v1.file.views import FileViewSet

projectRouter = ProjectRouter()
fileRouter = FileRouter()

projectRouter.register('projects', ProjectViewSet, basename='projects')
fileRouter.register('files', FileViewSet, basename='files')

urlpatterns = [
    path('v1/', include(projectRouter.urls)),
    path('v1/', include(fileRouter.urls))
]