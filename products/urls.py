from django.urls import path
from products import views
urlpatterns = [

    path('', views.getProducts, name="products"),

    path('create/', views.createProduct, name="product-create"),
    path('upload/', views.uploadImage, name="image-upload"),

    path('mystore/', views.getStoreProducts, name='store-products'),
    path('<int:pk>/', views.getProduct, name="product"),

    path('update/<int:pk>/', views.updateProduct, name="product-update"),
    path('delete/<int:pk>/', views.deleteProduct, name="product-delete"),
]
