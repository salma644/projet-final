"""src URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
#from django.contrib.auth import views as auth_views
from appli import views as appli_views
from django.conf import settings
from django.conf.urls.static import static
#from appli import views
from . import forms
#from django.views.generic import TemplateView
from django.views.generic.base import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include("appli.urls")),
    #path("", include("django.contrib.auth.urls")),
    #path('login/', appli_views.login, name='login'),
    #path('login/', TemplateView.as_view(template_name="about.html"), {'authentication_form': forms.LoginForm},name = 'login'),
   # path('logout/', views.logout, name = 'logout'),
    #path('', views.index, name='index'),
    #path("insert_data", views.insert_data,  name="insert_data"),
    #path("update_data<int:id>", views.update_data,  name="update_data"),
    #path("delete_data<int:id>", views.delete_data,  name="delete_data"),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
