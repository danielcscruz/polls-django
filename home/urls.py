from django.urls import path

from . import views



urlpatterns = [
    path('', views.index, name='index'),
    path('logout/', views.logout_view, name='logout_view'),
    path('login/', views.login_view, name='login_view'),
    path('register/', views.register, name='register')

]