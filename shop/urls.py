from django.views.generic import TemplateView
from django.urls import path, include
from shop import views
from main import settings
from django.conf.urls.static import static
urlpatterns = [
    path('', views.ProductsListView.as_view(), name='shop'),
    path('cart_view/', views.cart_view, name='cart_view'),
    path('detail/<int:pk>/', views.ProductsDetailView.as_view(), name='shop_detail'),
    path('add-item-to-cart/<int:pk>', views.add_item_to_cart, name='add_item_to_cart'),
    path('delete_item/<int:pk>', views.CartDeleteItem.as_view(), name='cart_delete_item'),
    path('make-order/', views.make_order, name='make_order'),

]
if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        path('__debug__/', include('debug_toolbar.urls')),
    ] + urlpatterns
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
