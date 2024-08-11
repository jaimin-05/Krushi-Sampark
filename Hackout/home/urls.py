from django.contrib import admin
from django.urls import path, include
from home import views

urlpatterns = [
    path('login', views.login_view, name="login_view"),
    path('', views.index, name="index"),
    path('signup', views.signup_view, name="signup_view"),
    path('farmer_index', views.farmer_index, name="farmer_index"),
    path('mill_index', views.mill_index, name="mill_index"),
    path('company_index', views.company_index, name="company_index"),
    path('cold_storage_index', views.cold_storage_index, name="cold_storage_index"),
    path('logout_view', views.logout_view, name='logout_view'),
    path('a_index', views.a_index, name='a_index'),  # Removed the extra comma here
    path('a1_index', views.a1_index, name='a1_index')
]   
