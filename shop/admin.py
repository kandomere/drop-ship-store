from django.contrib import admin

# Register your models here.
from shop.models import Product, Payment, OrderItem, Order, AboutUsPhoto

admin.site.register(Product)
admin.site.register(Payment)
admin.site.register(OrderItem)
admin.site.register(Order)
admin.site.register(AboutUsPhoto)

