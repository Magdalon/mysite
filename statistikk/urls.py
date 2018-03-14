from django.urls import path

from . import views

app_name = 'statistikk'

urlpatterns = [
    path('', views.index, name='index'),
    path('datasett/<int:pk>', views.DatasettView.as_view(), name= 'datasett')
]
