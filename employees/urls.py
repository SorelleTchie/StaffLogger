from django.urls import path
from . import views

urlpatterns=[
    path('', views.landing_page, name="landing_page"),
    path('new_employees/',views.new_employees, name='new_employees'),
    path('check_in/', views.check_in, name='check_in'),
    path('check_out/', views.check_out, name='check_out'),
    
]