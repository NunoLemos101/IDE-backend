from django.urls import path, include

from filesystem.api.v1.project.router import ProjectRouter
from filesystem.api.v1.project.views import ProjectViewSet

projectRouter = ProjectRouter()
projectRouter.register('projects', ProjectViewSet, basename='projects')

urlpatterns = [
    path('v1/', include(projectRouter.urls))
]