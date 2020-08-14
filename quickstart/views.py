from django.shortcuts import render
from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework import permissions

from snippets.models import Snippet
from .serializers import UserSerializer, GroupSerializer


# Create your views here.
# using viewsets keeps the view logic nicely organized as well as being very concise.
class UserViewSet(viewsets.ModelViewSet):
    """View and edit users."""

    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class GroupViewSet(viewsets.ModelViewSet):
    """View and edit users."""

    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]
