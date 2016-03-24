from django.conf.urls import include, url

from rest_framework import routers

from bookswap.users.views import UserViewSet

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)

urlpatterns = [
    url(r'^v1/', include(router.urls)),
]
