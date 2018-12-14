from django.urls import path,re_path,include
from . import views
from django.views.generic.base import RedirectView

app_name = 'helper'
urlpatterns = [
    path('search/', include('haystack.urls')),
    # policy views
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/details/', views.DetailView.as_view(), name='details'),
    path('add/', views.PolicyCreate.as_view(), name='create'),
    path('<int:pk>/edit', views.PolicyUpdate.as_view(), name='edit'),
    path('<int:pk>/delete', views.PolicyDelete.as_view(), name='delete'),
    re_path(r'^policies/(?P<datefrom>[0-9]{4}-[0-9]{2}-[0-9]{2})&(?P<dateto>[0-9]{4}-[0-9]{2}-[0-9]{2})', views.PolicyList.as_view(), name='policies'),
    re_path(r'^all_policies/(?P<datefrom>[0-9]{4}-[0-9]{2}-[0-9]{2})&(?P<dateto>[0-9]{4}-[0-9]{2}-[0-9]{2})', views.AllPolicyList.as_view(), name='all_policies'),
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
    # insurer add view
    path('insurers/', views.InsurerList.as_view(), name='insurer_list'),
    path('insurers/add/', views.InsurerCreate.as_view(), name='insurer_add'),
    # stats view
    path('stats/', views.StatisticsView.as_view(), name='statistics'),
    # autocomplete urls
    re_path(r'^client-autocomplete/$', views.ClientAutocomplete.as_view(), name='client-autocomplete'),
    re_path(r'^vehicle-autocomplete/$', views.VehicleAutocomplete.as_view(), name='vehicle-autocomplete'),
]
