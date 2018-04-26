from django.urls import path, include
from . import views

app_name = 'vue_test'
urlpatterns = [
    path('', views.index.as_view(), name='index'),
    path('other/', views.other.as_view(), name='other'),
]