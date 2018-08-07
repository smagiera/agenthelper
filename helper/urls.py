from django.urls import path
from . import views

app_name = 'helper'
urlpatterns = [
    # policy views
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/details/', views.DetailView.as_view(), name='details'),
    path('add/', views.PolicyCreate.as_view(), name='create'),
    path('<int:pk>/edit', views.PolicyUpdate.as_view(), name='edit'),
    path('<int:pk>/delete', views.PolicyDelete.as_view(), name='delete'),
    path('policies/', views.PolicyList.as_view(), name='all_policies'),
    # vehicle views
    path('vehicles/', views.VehicleList.as_view(), name='vehicles'),
    path('vehicles/<int:pk>/', views.VehicleDetail.as_view(), name='vehicle_details'),
    path('vehicles/<int:pk>/edit', views.VehicleUpdate.as_view(), name='vehicle_edit'),
    path('vehicles/<int:pk>/delete', views.VehicleDelete.as_view(), name='vehicle_delete'),
    path('vehicles/add', views.VehicleCreate.as_view(), name='vehicle_add'),
    # client views
    path('clients/', views.ClientList.as_view(), name='clients'),
    path('clients/<int:pk>/', views.ClientDetail.as_view(), name='client_details'),
    path('clients/<int:pk>/edit', views.ClientUpdate.as_view(), name='client_edit'),
    path('clients/<int:pk>/delete', views.ClientDelete.as_view(), name='client_delete'),
    path('clients/add', views.ClientCreate.as_view(), name='client_add'),    
]