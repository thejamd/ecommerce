from django.shortcuts import render,get_object_or_404
from django.shortcuts import render,redirect
from django.views import View
from .cart import Cart
from store.models import Products
from django.http import JsonResponse
class CartSummaryView(View):
    def get(self, request, *args, **kwargs):
        cart =Cart(request)
        cart_products = cart.get_prods
        quantities = cart.get_quants
        return render(request, 'cart_summary.html', {"cart_products":cart_products,"quantities":quantities})
def cart_add(request):
    #get the cart
    cart =Cart(request)
    #test for POST
    if request.POST.get('action') == 'post':
        product_id = int(request.POST.get('product_id'))
        product_qty = int(request.POST.get('product_qty'))
        #lookup product in the db
        products =get_object_or_404(Products,id=product_id)
        #save to session
        cart.add(product=products, quantity= product_qty)
        cart_quantity=cart.__len__()
        #return response
        response = JsonResponse({'qty': cart_quantity})
        # response = JsonResponse({'product_name': products.name})
        return response
def cart_delete(request):
    cart =Cart(request)
    if request.POST.get('action') == 'post':
        product_id = int(request.POST.get('product_id'))
        cart.delete(product = product_id)
        response = JsonResponse({'product': product_id})
        return response
def cart_update(request):
    cart =Cart(request)
    if request.POST.get('action') == 'post':
        product_id = int(request.POST.get('product_id'))
        product_qty = int(request.POST.get('product_qty'))
        cart.update(product = product_id, quantity = product_qty)
        response = JsonResponse({'qty': product_qty})
        return response
    # return redirect('cart_summary')