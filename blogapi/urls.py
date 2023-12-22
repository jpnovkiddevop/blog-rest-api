from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('articles', views.ArticleViewset, basename='articles')
router.register('users', views.UserViewset, basename='users')

urlpatterns = [
    path('api/', include(router.urls)),
]