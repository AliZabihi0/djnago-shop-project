from django.urls import path
from . import views

app_name = 'product'

urlpatterns = [
    path('detail/<int:pk>', views.ProductDetailView.as_view(), name='product_detail'),
    path('list', views.ProductView.as_view(), name='product_list'),
    path('search/', views.search_product, name='search'),
]
