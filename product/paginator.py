from django.core.paginator import Paginator


def paginator_list(request,products):
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
    return page_obj,page_range