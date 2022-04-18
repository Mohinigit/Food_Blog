"""blog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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

from django.urls import path
from . import views
#from django.contrib.auth.views import login

urlpatterns = [
        path('', views.home , name='home'),
        path('login/',views.login_view , name='login_view'),
        path('register/',views.register , name='register'),
        path('add-blog/',views.add_blog , name='add_blog'),
        path('blog-detail/<slug>',views.blog_detail,name='blog_detail'),
        path('see-blog/',views.see_blog, name='see_blog'),
        path('blog-delete/<id>',views.blog_delete, name='blog_delete'),
        path('blog-update/<slug>',views.blog_update, name='blog_update'),
        path('logout-view/',views.logout_view, name='logout_view')
]

