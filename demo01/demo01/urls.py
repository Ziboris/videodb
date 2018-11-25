"""demo01 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.urls import path
from django.conf.urls import url
from app01 import views

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^index/',views.index,name="index"),
    path('detail/<str:name>/<int:case_id>/',views.detail,name="detail"),

    url(r'^autoEdit/',views.autoEdit,name="autoEdit"),
    path('delete/<int:counter>/', views.delete, name='delete'),
    path('para/',views.para,name="para"),
    path("download/",views.download,name="download"),

    url(r'^tag/',views.tag,name="tag"),
    url(r'^contactus/',views.contactus,name="contactus"),
    
    # 视频库
    # url(r'^repo/$',views.repo_base,name="repo_base"),
    # url(r'^repo/type$',views.repo_1,name="repo_type"),
    # url(r'^repo/style$',views.repo_2,name="repo_style"),
    # url(r'^repo/business$',views.repo_3,name="repo_business"),
    # url(r'^repo/media$',views.repo_4,name="repo_media"),
    # url(r'^repo/year$',views.repo_5,name="repo_year"),
    # url(r'^repo/consumer$',views.repo_6,name="repo_consumer"),
    #
    # url(r'^case_change/$',views.case_change,name="case_change"),
    # url(r'^upload_material/',views.upload_material,name="upload_material"),
    # url(r'^analyzing/$',views.analyzing,name='analyzing'),
    # url(r'^display_case_parameter/',views.display_case_parameter,name='parameter'),
    #
    # url(r'show/',views.show,name='show'),
    # url(r'test1/',views.test1,name="test1"),
    # url(r'test2/',views.test2,name="test2"),
    # url(r'test3/',views.test3,name="test3"),
    
]
