from django.urls import path, include
from .views import AppCreateView, AppListView, delete_app


urlpatterns = [
    path('create-app/', AppCreateView.as_view() , name='create-app'),
    path('apps/<slug:slug>/delete-app/', delete_app, name='delete-app'),
    path('apps/', AppListView.as_view(), name='apps'),
    path('apps/<slug:slug>/', include('customers.urls')),
]