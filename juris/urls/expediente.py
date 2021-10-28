from django.urls import path

from juris.views.expedientes import ExpedienteDetailView, ExpedienteListView

urlpatterns = [
    path('', ExpedienteListView.as_view(), name="expediente-list"),
    path('<int:pk>/', ExpedienteDetailView.as_view(),
         name="expediente-detail"),
]
