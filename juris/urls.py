from django.urls import path
from . import views

urlpatterns = [
    path('index', views.index, name='index'),
    path('',views.ExpedienteListView.as_view(), name="expedientes"),
    path('<int:pk>', views.ExpedienteDetailView.as_view(), name="expediente-detail" ),
    path('expediente/<int:pk>', views.ActualizacionListView.as_view(), name="acttualizaciones"),
]