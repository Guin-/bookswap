from django.conf.urls import include, url

from rest_framework import routers

from bookswap.users.views import UserViewSet
from bookswap.books.views import BookViewSet

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'books', BookViewSet)

urlpatterns = [
    url(r'^v1/', include(router.urls)),
]
