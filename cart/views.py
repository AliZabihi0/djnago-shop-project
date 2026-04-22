from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.http import JsonResponse
from cart.cart_module import Cart
from cart.models import OrderItem, Order, DiscountCode
from product.models import Product, Size, Color


class CartView(View):
    def get(self, request):
        cart = Cart(request)
        return render(request, "cart/shop_cart.html", {'cart': cart})


class AddCartView(View):
    def post(self, request, pk):
        product = get_object_or_404(Product, id=pk)
        size, color, quantity = request.POST.get('size'), request.POST.get('color'), request.POST.get('quantity')
        cart = Cart(request)
        cart.add(product, quantity, size, color)
        return redirect("cart:shop_cart")


class RemoveCartView(View):
    def get(self, request, id):
        cart = Cart(request)
        cart.delete(id)
        return redirect("cart:shop_cart")


class OrderCartView(View):
    def get(self, request, id):
        order = get_object_or_404(Order, id=id)
        return render(request, "cart/shop_checkout.html", {'order': order})


class OrderCreateView(View):
    def get(self, request):
        cart = Cart(request)
        order = Order.objects.create(user=request.user, total=cart.total())
        for product in cart:
            print(product)
        for item in cart:
            OrderItem.objects.create(order=order, quantity=item['quantity'], product=item['product'], size=item["size"],
                                     color=item["color"], price=item['price'])
        return redirect("cart:checkout", order.id)


class DiscountOrderView(View):
    def post(self, request, id):
        order = get_object_or_404(Order, id=id)
        discount = request.POST.get('discount')
        discount_code = get_object_or_404(DiscountCode, name=discount)
        order.total -= order.total * discount_code.discount/100
        order.save()
        discount_code.quantity -= 1
        discount_code.save()
        return redirect("cart:checkout", order.id)
