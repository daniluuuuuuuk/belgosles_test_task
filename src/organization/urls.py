from django.urls import path

from .views import *

urlpatterns = [
    path('', OrganizationHome.as_view(), name='orgs'),
    path('keys/', index, name='keys'),
    path('del_org/<int:pk>/', delete_org, name="del_org"),
    path('create_org/', create_org, name="create_org"),
    path('update_org/<int:pk>/', update_org, name="update_org"),
    path('del_key/<int:pk>/', delete_key, name="del_key"),
    path('create_key/', create_key, name="create_key"),
    path('update_key/<int:pk>/', update_key, name="update_key"),
]
