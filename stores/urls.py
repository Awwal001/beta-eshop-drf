from django.urls import path
from stores import views


urlpatterns = [

    path('', views.getStores, name='stores'),
    path('create/', views.createStore, name='create-store'),
    

    path('<int:pk>/', views.getOneStore, name="get-store"),
    path('update/<int:pk>/', views.updateStore, name="store-update"),
    path('delete/<int:pk>/', views.deleteStore, name="store-delete"),
]
