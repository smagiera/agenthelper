from django.urls import path
from . import views

app_name = 'helper'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/details/', views.DetailView.as_view(), name='details'),
    path('add/', views.PolicyCreate.as_view(), name='create'),
    path('<int:pk>/edit', views.PolicyUpdate.as_view(), name='edit'),
    path('<int:pk>/delete', views.PolicyDelete.as_view(), name='delete')
]