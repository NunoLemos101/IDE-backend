from rest_framework.routers import SimpleRouter, Route


class FileRouter(SimpleRouter):

    routes = [
        Route(
            url=r'^{prefix}/$',
            mapping={'post': 'create'},
            name='{basename}-detail',
            detail=True,
            initkwargs={}
        ),
        Route(
            url=r'^{prefix}/{lookup}/save/$',
            mapping={'put': 'save'},
            name='{basename}-detail',
            detail=True,
            initkwargs={}
        ),
    ]