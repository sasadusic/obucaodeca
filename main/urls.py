from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('register/', views.register_user, name='register'),
    path('profile/', views.profile, name='profile'),
    path('update_profile/', views.update_profile, name='update_profile'),
    path('change_password/', views.change_password, name='change_password'),
    path('delete_profile/', views.delete_profile, name='delete_profile'),
    
    path('kreiraj_obucu/', views.kreiraj_obucu, name='kreiraj_obucu'),
    path('sva_obuca/', views.sva_obuca, name='sva_obuca'),
    path('detalji_obuce/<int:pk>/', views.detalji_obuce, name='detalji_obuce'),
]