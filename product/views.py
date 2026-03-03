from django.shortcuts import render
from django.views.generic import DetailView, ListView

from product.models import Product


class ProductDetailView(DetailView):
    model = Product
    template_name = 'product/product_detail.html'

class ProductListView(ListView):
    model = Product
    template_name = 'product/product_list.html'
    queryset = Product.objects.all()
    paginate_by = 1