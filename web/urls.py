from django.urls import path
from .views import index

app_name = "web"

urlpatterns = [
    path(r'', index, name='index'),
]
