# from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
# from .models import Product
from .models import Order

@login_required
def home(request):
 return render(request, "home.html", {})


def authView(request):
 if request.method == "POST":
  form = UserCreationForm(request.POST or None)
  if form.is_valid():
   form.save()
   return redirect("base:login")
 else:
  form = UserCreationForm()
 return render(request, "registration/signup.html", {"form": form})



def product_list(request):
    search_query = request.GET.get('search', '')
    sort_by = request.GET.get('sort', 'name')

    products = Product.objects.all()

    if search_query:
        products = products.filter(name__icontains=search_query)

    if sort_by in ['name', 'price', 'created_at']:
        products = products.order_by(sort_by)

    context = {
        'products': products,
        'search_query': search_query,
        'sort_by': sort_by,
    }
    return render(request, 'product_list.html', context)

def user_orders(request):
    # Отримуємо всі ордери поточного користувача
    orders = Order.objects.filter(user=request.user).order_by('-created_at')
    return render(request, 'user_orders.html', {'orders': orders})

from django.shortcuts import render, get_object_or_404, redirect
from .models import Product

def product_list_test(request):
    products = Product.objects.all()
    return render(request, 'product_list_test.html', {'products': products})

def product_detail(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    return render(request, 'product_detail.html', {'product': product})

def add_to_cart(request, product_id):
    cart = request.session.get('cart', {})
    if product_id in cart:
        cart[product_id] += 1
    else:
        cart[product_id] = 1
    request.session['cart'] = cart
    return redirect('cart_detail')

def cart_detail(request):
    cart = request.session.get('cart', {})
    cart_items = []
    total_price = 0
    for product_id, quantity in cart.items():
        product = get_object_or_404(Product, id=product_id)
        total_price += product.price * quantity
        cart_items.append({'product': product, 'quantity': quantity})
    return render(request, 'cart_detail.html', {'cart_items': cart_items, 'total_price': total_price})
