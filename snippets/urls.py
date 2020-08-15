from django.urls import path, include
from rest_framework.urlpatterns import format_suffix_patterns

from . import views

urlpatterns = format_suffix_patterns([

    path('', views.api_root),
    path('snips/', views.SnippetList.as_view(), name='snippet-list'),
    path('snips/<int:pk>/', views.SnippetDetail.as_view(), name='snippet-detail'),
    path('snips/<int:pk>/highlight/', views.SnippetHighlight.as_view(), name='snippet-highlight'),
    path('users/', views.UserList.as_view(), name='user-list'),
    path('users/<int:pk>/', views.UserDetail.as_view(), name='user-detail'),
])
