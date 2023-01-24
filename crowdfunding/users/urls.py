from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
    path('', views.CustomUserList.as_view(), name='customer-list'),
    path('users/<int:pk/', views.CustomUserDetail.as_view(), name='customeruser-detail')
]