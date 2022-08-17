from django.urls import path
from orders import views


urlpatterns = [

    path('', views.getOrders, name='orders'),
    path('add/', views.addOrderItems, name='orders-add'),
    path('myorders/', views.getMyOrders, name='myorders'),
    path('store-orders/<int:store_id>/', views.getOrderByStore, name='store-orders'),

    path('<int:pk>/deliver/', views.updateOrderToDelivered, name='order-delivered'),

    path('<int:pk>/', views.getOrderById, name='user-order'),
    path('<int:pk>/pay/', views.updateOrderToPaid, name='pay'),
]
