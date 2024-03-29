from rest_framework.routers import SimpleRouter, Route


class ProjectRouter(SimpleRouter):

    routes = [
        Route(
            url=r'^{prefix}/{lookup}/filesystem/$',
            mapping={'get': 'retrieve'},
            name='{basename}-detail',
            detail=True,
            initkwargs={}
        ),
        Route(
            url=r'^{prefix}/{lookup}/build/$',
            mapping={'post': 'build'},
            name='{basename}-detail',
            detail=True,
            initkwargs={}
        ),
    ]