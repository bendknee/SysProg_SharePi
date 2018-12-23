from django.urls import path
from .views import index, file_form, file_post, file_view, request_access

app_name = "web"

urlpatterns = [
    path(r'', index, name='index'),
    path(r'upload', file_form, name='file_form'),
    path(r'upload_post', file_post, name='file_post'),
    path(r'view', file_view, name='file_view'),
    path(r'verification', request_access, name='request_access')
]
