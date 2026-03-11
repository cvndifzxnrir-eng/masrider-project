from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('riders/', views.rider_list, name='rider_list'),
    path('riders/new/', views.rider_create, name='rider_create'),
    path('riders/<int:pk>/', views.rider_detail, name='rider_detail'),
    path('riders/<int:pk>/edit/', views.rider_update, name='rider_update'),
    path('riders/<int:pk>/delete/', views.rider_delete, name='rider_delete'),
    path('riders/<int:rider_pk>/competition/add/', views.competition_add, name='competition_add'),
    path('competition/<int:pk>/delete/', views.competition_delete, name='competition_delete'),
    path('riders/<int:rider_pk>/ability/add/', views.ability_add, name='ability_add'),
]
