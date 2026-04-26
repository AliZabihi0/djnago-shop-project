from django.core.paginator import Paginator
from django.shortcuts import render
from django.views import View
from django.views.generic import DetailView, ListView, FormView


from .paginator import paginator_list

from product.models import Product


class ProductDetailView(DetailView):
    model = Product
    template_name = 'product/product_detail.html'

class ProductView(View):
    def get(self, request):
        products = Product.objects.all()
        page_obj,page_range=paginator_list(request,products)
        return render(request, 'product/product_list.html', {'product_list': page_obj ,'page_range': page_range})


def search_product(request):
    q = request.GET.get('q')
    products = Product.objects.filter(name__icontains=q)
    page_obj, page_range = paginator_list(request, products)
    return render(request, 'product/product_list.html', {'product_list': page_obj ,'page_range': page_range})




