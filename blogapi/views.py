from django.contrib.auth.models import User
from .serializers import ArticleSerializer, UserSerializer
from .models import Article
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication

class ArticleViewset(viewsets.ModelViewSet):
    queryset = Article.objects.all() 
    serializer_class = ArticleSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = (TokenAuthentication,)


class UserViewset(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


