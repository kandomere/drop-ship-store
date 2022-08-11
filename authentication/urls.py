from django.urls import path, include
from authentication import views
urlpatterns = [
    path('login/', views.login_user, name='login'),
    path('register/', views.Register.as_view(), name='register'),
    path('logout/', views.logout_user, name='logout'),
]
