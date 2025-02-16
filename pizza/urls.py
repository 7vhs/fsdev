from django.urls import path
from . import views

urlpatterns = [
   path('', views.index, name='index'),
   path('previous/', views.previous, name='previous'),
   path('create/', views.create_pizza, name='create'),
   path('delivery/', views.delivery, name='delivery'),
   path('final/', views.final, name='final'),
   path('login/', views.login_view, name='login'),
   path('signup/', views.signup, name='signup'),
   path('logout/', views.logout_view, name='logout'),
   path('createuser/', views.create_user, name='create_user'),
   path('updateuser/<str:userem>/', views.update_user, name='update_user'),
]