from .views import CategoryViewSet, PostViewSet, AuthorViewSet
from rest_framework.routers import DefaultRouter
from django.urls import path, include

router = DefaultRouter()
router.register('author', AuthorViewSet, basename='author')
router.register('post', PostViewSet, basename='post')
router.register('category', CategoryViewSet, basename='category')

urlpatterns = [
    path('api/', include(router.urls))
]
