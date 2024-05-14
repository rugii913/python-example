"""
URL configuration for django_basic project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
# urls.py는 url 요청 경로를 기반으로 어디로 보낼지, 어떤 함수를 실행시킬지 등을 정의해두는 파일
from shortener.views import index, get_user
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls), # Django가 이미 만들어준 url
    path("", index, name="index"), # name은 redirect 등을 위해 필요한 이름
    path("users/<int:user_id>", get_user), # path variable 넘길 수 있음
]
