from django.contrib import admin
from django.urls import path,include
from django.contrib.auth import views as user

urlpatterns = [
    path('phansivang/', admin.site.urls),
    path('',include('app.urls')),
    path('login/',user.LoginView.as_view(template_name='app/login.html'),name='login'),
path('logout/',user.LogoutView.as_view(template_name='app/login.html'),name='logout'),

]
