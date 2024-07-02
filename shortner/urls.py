from django.urls import path
from . import views

urlpatterns = [
    path('res/<str:pk>', views.res, name='res'),
    path('edit/<str:uuid>/', views.url_edit, name='url_edit'),
    path('delete/<str:uuid>/', views.url_delete, name='url_delete'),
    path('u/<str:pk>', views.go, name='go'),
    path('', views.index, name='index'),
]
