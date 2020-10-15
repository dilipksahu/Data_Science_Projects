
from django.urls import path
from . import views

urlpatterns = [
    path('inquary',views.inquary,name='inquary'),
]
