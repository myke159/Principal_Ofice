from django.urls import path

# Autenticador padrao django login e logout
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('login/', auth_views.LoginView.as_view(
    template_name='usuarios/login.html'
    ), name="login"),
    path('logout/', auth_views.LogoutView.as_view(), name="logout")
]