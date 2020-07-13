from django.conf.urls import url
from django.urls import include
from rest_framework import routers
from .models import BookViewSet

# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'book', BookViewSet)

# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^book/', include('rest_framework.urls', namespace='rest_framework'))
]