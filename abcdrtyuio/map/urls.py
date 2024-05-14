from django.urls import path
from.import views

urlpatterns = [
   path('', views.map_home, name='map_home'),
   path('post/<int:post_id>/', views.show_post, name='post'),
   path('category/<int:cat_id>/', views.show_category, name='category'),
   path('addrecept', views.addrecept, name='addrecept'),
   path('login', views.LoginUser.as_view(), name='login'),
   path('logout', views.logout_user, name='logout'),
   path('register', views.RegisterUser.as_view(), name='register'),
]