from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<str:pk>', views.go , name='go'),
    path('res/<str:pk>', views.res , name='res'),
]