from django.urls import path
from django.urls.conf import include
from juris import views

urlpatterns = [
    path('', views.index, name='index'),
    path('expedientes/', include('juris.urls.expediente')),
]