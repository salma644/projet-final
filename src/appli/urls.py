from django.urls import path,include
from . import views

#app_name = 'appli' # So we can use it like: {% url 'mymodule:user_login' %} on our template.
urlpatterns = [
    
    path("",views.base, name="base"),
    path('register/', views.registerPage, name="register"),
    path('login/', views.loginPage, name="login"),
    path('dashboard/', views.dash, name="dashboard"),
    path('index/', views.index, name='index'),
    path('virtual/', views.virtual, name='vm'),
    path('index0/', views.userlist, name='userges'),
    #path('index1/', views.index1, name='index1'),
    path('index2/', views.index2, name='index2'),
    path('index3/', views.index3, name='index3'),
    #path('index4/', views.indexvm, name='index4'),
    path('registerus', views.register, name="registerus"),
    path('logout/', views.logoutUser, name="logout"),
    path("insert_data", views.insert_data,  name="insert_data"),
    path("insert_data_user", views.insert_data_user,  name="insert_datau"),
    path("update_data/<int:id>/<str:Name>", views.update_data,  name="update_data"),
    path("update_data_user/<int:id>/<str:Name>", views.update_data_user,  name="update_data_user"),
    path("delete_data/<int:id>/<str:Name>", views.delete_data,  name="delete_data"),
    #path("insert_data1", views.insert_data1,  name="insert_data1"),
    #path("update_dataa<int:id>", views.update_dataa,  name="update_dataa"),
    #path("delete_dataa<int:id>", views.delete_dataa,  name="delete_dataa"),
    path("insert_datan", views.insert_datan,  name="insert_datan"),
    path("update_datan<int:id>", views.update_datan,  name="update_datan"),
    path("delete_datan<int:id>", views.delete_datan,  name="delete_datan"),
    path("insert_datah", views.insert_datah,  name="insert_datah"),
    path("update_datah<int:id>", views.update_datah,  name="update_datah"),
    path("delete_datah<int:id>", views.delete_datah,  name="delete_datah"),
    path("start/<int:id>/<str:Name>", views.start,  name="start"),
    path("shutdown/<int:id>/<str:Name>", views.shutdown,  name="shutdown"),
    path("userdel<int:id>", views.userdel,  name="userdelete"),
    path("userupd<int:id>", views.userupd,  name="userupdate"), 
    
]
