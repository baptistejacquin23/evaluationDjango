from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('create', views.create, name='create'),
    path('<int:pk>', views.detail, name='detail'),
    path('update/<int:pk>', views.update, name='update'),
]
