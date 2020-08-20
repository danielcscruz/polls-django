from django.urls import path
from . import views


app_name = 'loto'
urlpatterns = [
    path('', views.loto_generator, name='loto_generator'),
    path('output/', views.output, name='output'),

]