from django.core.paginator import Paginator
from django.shortcuts import render
from django.views import View
from django.views.generic import DetailView, ListView

from product.models import Product


class ProductDetailView(DetailView):
    model = Product
    template_name = 'product/product_detail.html'

class ProductView(View):
    # model = Product
    # template_name = 'product/product_list.html'
    # queryset = Product.objects.all()
    # paginate_by = 1
    def get(self, request):
        products = Product.objects.all()
        page_number = request.GET.get('page')
        paginator = Paginator(products, 1)
        page_obj = paginator.get_page(page_number)
        # page_limit
        page_limit = 3
        current_page = page_obj.number
        total_pages = paginator.num_pages
        start_page = max(current_page - 1, 1)
        end_page = min(start_page + page_limit - 1, total_pages)
        if end_page - start_page < page_limit:
            start_page = max(end_page - page_limit + 1, 1)
        page_range = range(start_page, end_page + 1)
        return render(request, 'product/product_list.html', {'product_list': page_obj ,'page_range': page_range})


def search_product(request):
    q = request.GET.get('q')
    products = Product.objects.filter(name__icontains=q)
    return render(request, 'product/product_list.html', {'product_list': products})