from django.urls import path

from . import views

app_name = 'afrikaquiz'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('longest/', views.longest, name='longest'),
    path('list/', views.IndexView.as_view(), name='list'),
    path('random/', views.random, name='random'),
    path('country/<str:iso>/', views.detail, name='detail'),
    path('country/<str:iso>/<int:pid>/result/',views.result, name='result'),
    path('country/<str:iso>/vote', views.vote, name='vote'),

]
