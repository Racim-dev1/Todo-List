from django.contrib import admin
from django.urls import path ,include
from django.contrib.auth import views as auth_views
from todos import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/',include('users.urls')),
    path('register/', views.registerPage, name='register'),
    path('', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('todos/',include('todos.urls'))
]
