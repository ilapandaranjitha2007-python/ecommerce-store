from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.shortcuts import render, get_object_or_404, redirect
from .models import Product, Order, OrderItem


def product_list(request):
    products = Product.objects.all()

    return render(request, 'store/product_list.html', {
        'products': products
    })


def product_detail(request, id):
    product = get_object_or_404(Product, id=id)

    return render(request, 'store/product_detail.html', {
        'product': product
    })


def add_to_cart(request, id):
    product = get_object_or_404(Product, id=id)

    cart = request.session.get('cart', {})

    product_id = str(product.id)

    if product_id in cart:
        cart[product_id] += 1
    else:
        cart[product_id] = 1

    request.session['cart'] = cart

    return redirect('cart')


def cart(request):
    cart = request.session.get('cart', {})

    products = []
    total = 0

    for product_id, quantity in cart.items():

        product = get_object_or_404(Product, id=product_id)

        item_total = product.price * quantity
        total += item_total

        products.append({
            'product': product,
            'quantity': quantity,
            'item_total': item_total
        })

    return render(request, 'store/cart.html', {
        'products': products,
        'total': total
    })
def register(request):

    if request.method == 'POST':

        username = request.POST['username']
        password = request.POST['password']

        if User.objects.filter(username=username).exists():
            return render(request, 'store/register.html', {
                'error': 'Username already exists.'
            })

        user = User.objects.create_user(
            username=username,
            password=password
        )

        login(request, user)

        return redirect('product_list')

    return render(request, 'store/register.html')


def login_view(request):

    if request.method == 'POST':

        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(
            request,
            username=username,
            password=password
        )

        if user is not None:
            login(request, user)
            return redirect('product_list')

        return render(request, 'store/login.html', {
            'error': 'Invalid username or password.'
        })

    return render(request, 'store/login.html')


def logout_view(request):

    logout(request)

    return redirect('product_list')
def checkout(request):
    if not request.user.is_authenticated:
        return redirect('login')

    cart = request.session.get('cart', {})

    if not cart:
        return redirect('cart')

    # Check stock before placing order
    for product_id, quantity in cart.items():
        product = get_object_or_404(Product, id=product_id)

        if quantity > product.stock:
            return render(request, 'store/checkout.html', {
                'error': f'{product.name} has only {product.stock} items available.'
            })

    if request.method == 'POST':
        name = request.POST['name']
        address = request.POST['address']
        phone = request.POST['phone']

        total = 0

        # Calculate total
        for product_id, quantity in cart.items():
            product = get_object_or_404(Product, id=product_id)

            total += product.price * quantity

        # Create order
        order = Order.objects.create(
            user=request.user,
            name=name,
            address=address,
            phone=phone,
            total_amount=total
        )

        # Create order items and reduce stock
        for product_id, quantity in cart.items():

            product = get_object_or_404(
                Product,
                id=product_id
            )

            OrderItem.objects.create(
                order=order,
                product=product,
                quantity=quantity,
                price=product.price
            )

            product.stock -= quantity
            product.save()

        # Clear cart
        request.session['cart'] = {}

        return render(
            request,
            'store/order_success.html',
            {'order': order}
        )

    return render(request, 'store/checkout.html')
def order_history(request):

    if not request.user.is_authenticated:
        return redirect('login')

    orders = Order.objects.filter(
        user=request.user
    ).order_by('-created_at')

    return render(request, 'store/order_history.html', {
        'orders': orders
    })
def increase_quantity(request, id):
    cart = request.session.get('cart', {})
    product_id = str(id)

    product = get_object_or_404(Product, id=id)

    if product_id in cart:
        if cart[product_id] < product.stock:
            cart[product_id] += 1

    request.session['cart'] = cart

    return redirect('cart')

def decrease_quantity(request, id):
    cart = request.session.get('cart', {})
    product_id = str(id)

    if product_id in cart:
        if cart[product_id] > 1:
            cart[product_id] -= 1
        else:
            del cart[product_id]

    request.session['cart'] = cart

    return redirect('cart')


def remove_from_cart(request, id):
    cart = request.session.get('cart', {})
    product_id = str(id)

    if product_id in cart:
        del cart[product_id]

    request.session['cart'] = cart

    return redirect('cart')