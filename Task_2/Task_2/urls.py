"""
URL configuration for Task_2 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from app2 import views
from app2.views import GetEndpoint1, GetEndpoint2, PostEndpoint

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home),
    path('get1/', GetEndpoint1.as_view(), name='get_endpoint_1'),
    path('get2/', GetEndpoint2.as_view(), name='get_endpoint_2'),
    path('post/', PostEndpoint.as_view(), name='post_endpoint'),
]
