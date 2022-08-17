from django.urls import path
from accounts import views


urlpatterns = [
    path('login/', views.loginUser, name='login'),
    path('register/', views.registerUser, name='register'),

    path('users/', views.getUsers, name="users"),
    path('user/<int:pk>/', views.getUserById, name='user'),

    path('user/update/<int:pk>', views.updateUser, name='user-update'),

    path('user/delete/<int:pk>/', views.deleteUser, name='user-delete'),
]
