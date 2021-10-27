from django.urls import path
from . import views

urlpatterns = [
    path('index', views.index, name='index'),
    path('',views.ExpedienteListView.as_view(), name="expedientes"),
]