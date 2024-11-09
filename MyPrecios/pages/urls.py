from django.urls import path
from django.views.decorators.cache import cache_page
from django.urls import include, path
from rest_framework import routers

from .views import  MailsViewSet


class MyCustomRouter(routers.SimpleRouter):
   routes = [
      routers.Route(url=r'^{prefix}$',
                    mapping={'get': 'list'},
                    name='{basename}-list',
                    detail=False,
                    initkwargs={'suffix': 'List'}),
      routers.Route(url=r'^{prefix}/{lookup}$',
                    mapping={'get': 'retrieve'},
                    name='{basename}-detail',
                    detail=True,
                    initkwargs={'suffix': 'Detail'})
   ]

router = routers.SimpleRouter()
router.register(r'mails', MailsViewSet,basename='ails')


urlpatterns = [
   path('', include(router.urls))
]