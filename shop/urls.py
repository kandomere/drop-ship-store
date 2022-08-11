from django.views.generic import TemplateView
from django.urls import path, include
from authentication import views

urlpatterns = [
    path('', TemplateView.as_view(template_name='shop/shop.html'), name='shop'),
    path('cart_view/', TemplateView.as_view(template_name='shop/cart.html'), name='cart_view'),
    path('detail/<int:pk>/', TemplateView.as_view(template_name='shop/shop-details.html'), name='shop_detail'),

]
