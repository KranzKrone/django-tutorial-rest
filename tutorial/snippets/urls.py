from django.urls import path
from snippets import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('snippets/', views.SnippetList.as_view()),
    path('snippets/<pk>/', views.SnippetDetail.as_view(), name='snippet-detail'),    
    path('users/', views.UserList.as_view(), name='user-list'),
    path('users/<pk>/', views.UserDetail.as_view(), name='user-detail'),
    path('', views.api_root),
    path('snippets/<pk>/highlight/', views.SnippetHighlight.as_view(), name='snippet-highlight'),
]

urlpatterns = format_suffix_patterns(urlpatterns)
