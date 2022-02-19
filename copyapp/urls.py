from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('login/', views.login, name="login"),
    path('register/', views.register, name="register"),
    path('workspace/', views.workspace, name="workspace"),
    path('add-copy/', views.add_copy),
    path('logout/', views.logout, name="logout"),
] 