from django.contrib import admin
from .models import *
# Register your models here.
class OrderAdmin(admin.ModelAdmin):
    def get_readonly_fields(self, request, obj=None):
        if obj.isCanceled == False:
            return self.readonly_fields
        return ( 'shippingAddress','totalPrice','isPaid','isDelivered', 'isCanceled')

admin.site.register(Order, OrderAdmin)
admin.site.register(OrderItem)
