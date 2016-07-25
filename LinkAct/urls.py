"""TermProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/dev/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""

from django.conf.urls import url 
from . import views

urlpatterns = [
    url(r'^act_info/$', views.show_act),
    url(r'^personal_info/$', views.show_people),
    url(r'user/info/', views.check_personal_msg, name='user_info_url'),
    url(r'user/set_password/', views.set_password_func, name='user_password_url'),
    url(r'^linker/$', views.search_people, name='linker_page_url'),
    url(r'^activities/$', views.search_act, name='activities_page_url'),
    url(r'explore/', views.explore_page_show, name='explore_page_url'),
    url(r'share/', views.share_page_show, name='share_page_url'),
    url(r'login/', views.log_in, name='log_in_url'),
    url(r'register/', views.user_register, name='register_url'),
    url(r'^$', views.start_page_show, name='start_page_url'),
]
