from django.shortcuts import render

# Create your views here.
def cart(request):
    return render(request, 'cart/cart.html')

def place_order(request):
    return render(request, 'cart/place_order.html')