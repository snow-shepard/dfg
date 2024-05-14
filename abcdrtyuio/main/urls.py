from django.urls import path
from.import views

urlpatterns = [
   path('', views.index, name='home'),
   path('onas', views.onas, name='onas'),
   
]

