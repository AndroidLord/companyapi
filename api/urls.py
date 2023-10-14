from django.contrib import admin
from django.urls import path,include
from rest_framework import routers
from .views import CompanyViewSet,EmployeeViewSet

routers = routers.DefaultRouter()
routers.register(r'companies',CompanyViewSet)
routers.register(r'employies',EmployeeViewSet)

urlpatterns = [
            path('',include(routers.urls))
]