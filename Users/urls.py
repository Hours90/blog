from  django.urls import path

from django.contrib.auth.views import LoginView

from . import views

app_name = 'Users'
urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', LoginView.as_view(template_name ='Users/login.html'), name='login'),
    path('logout/', views.logout_view, name="logout"),
    path('profile/', views.profile, name = 'profile'),


    ]      