from django.urls import path
from . import views


app_name = 'cart'

urlpatterns = [
    path('cart', views.CartView.as_view(), name='shop_cart'),
    path('add/<int:pk>', views.AddCartView.as_view(), name='add_to_cart'),
    path('delete/<str:id>', views.RemoveCartView.as_view(), name='remove_cart'),
    path('order/add', views.OrderCreateView.as_view(), name='add_order'),
    path('<int:id>', views.OrderCartView.as_view(), name='checkout'),
    path('discount/<int:id>', views.DiscountOrderView.as_view(), name='discount_order'),

]
