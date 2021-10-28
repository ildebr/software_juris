from django.urls import path
from . import views

urlpatterns = [
    path('index', views.index, name='index'),
    path('',views.ExpedienteListView.as_view(), name="expedientes"),
    path('<int:expediente>', views.ExpedienteDetailView.as_view(), name="expediente-detail"),
    path('actualizacion/<int:pk>', views.ActualizacionDetailView.as_view(), name="actualizacion-detail-view"),
]