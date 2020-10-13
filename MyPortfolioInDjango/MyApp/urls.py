from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    # path('myskill',views.myskill,name='myskill'),
    # path('myservices',views.myservices,name='myservices'),
]