from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib import messages
from .models import MenuItem, Cart, CartItem, Order, OrderItem, ContactMessage, Profile
from .forms import ContactForm, UserProfileForm, CustomUserCreationForm
from django.http import JsonResponse
from django.views import View
from .forms import ProfileEditForm

def home(request):
    specials = MenuItem.objects.filter(is_special=True)[:4]
    categories = MenuItem.CATEGORY_CHOICES
    return render(request, 'orders/pages/home.html', {
        'specials': specials,
        'categories': categories
    })


def menu(request):
    category = request.GET.get('category', 'MAIN')
    menu_items = MenuItem.objects.filter(category=category, available=True)
    return render(request, 'orders/pages/menu.html', {
        'menu_items': menu_items,
        'categories': MenuItem.CATEGORY_CHOICES,
        'current_category': category
    })


@login_required
def cart(request):
    try:
        cart = Cart.objects.get(user=request.user)
        cart_items = cart.items.all()  # Get all items in the cart
        total = sum(item.total_price for item in cart_items)
    except Cart.DoesNotExist:
        cart_items = None
        total = 0

    return render(request, 'orders/pages/cart.html', {
        'cart_items': cart_items,  # Pass items to template
        'total_cost': total,       # Pass total cost
    })


@login_required
def add_to_cart(request, item_id):
    if request.method == 'POST':
        menu_item = get_object_or_404(MenuItem, id=item_id)
        cart, created = Cart.objects.get_or_create(user=request.user)

        cart_item, created = CartItem.objects.get_or_create(
            cart=cart,
            menu_item=menu_item,
            defaults={'quantity': 1}
        )

        if not created:
            cart_item.quantity += 1
            cart_item.save()

        if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
            # Return JSON for AJAX requests
            return JsonResponse({
                'success': True,
                'message': f"{menu_item.name} added to cart!",
                'cart_count': cart.items.count(),
            })
        else:
            # Redirect for normal form submissions
            messages.success(request, f"{menu_item.name} added to cart!")
            return redirect('orders')
    return JsonResponse({'success': False, 'error': 'Invalid request'}, status=400)


@login_required
def update_cart(request, cart_item_id):  # Changed parameter name
    cart_item = get_object_or_404(CartItem, id=cart_item_id, cart__user=request.user)

    if request.method == 'POST':
        new_quantity = int(request.POST.get('quantity', 1))

        if new_quantity < 1:
            cart_item.delete()
        else:
            cart_item.quantity = new_quantity
            cart_item.save()

    return redirect('cart')

@login_required
def remove_from_cart(request, item_id):
    cart_item = get_object_or_404(CartItem, id=item_id, cart__user=request.user)
    cart_item.delete()
    return redirect('cart')


@login_required
def clear_cart(request):
    cart = get_object_or_404(Cart, user=request.user)
    cart.items.all().delete()
    return redirect('cart')


@login_required
def checkout(request):
    try:
        cart = Cart.objects.get(user=request.user)
        cart_items = cart.items.all()
        total_cost = sum(item.total_price for item in cart_items)

        # Create the order only if there are items in the cart
        if cart_items.exists():
            profile = request.user.profile
            order = Order.objects.create(
                user=request.user,
                total=total_cost,
                delivery_address=profile.address,
                contact_number=profile.mobile_number,
                status='preparing'
            )

            # Create order items
            for cart_item in cart_items:
                OrderItem.objects.create(
                    order=order,
                    menu_item=cart_item.menu_item,
                    quantity=cart_item.quantity,
                    price=cart_item.menu_item.price
                )

        # Clear the cart after checkout
        cart.items.all().delete()

        return render(request, 'orders/pages/checkout.html', {
            'total_cost': total_cost,
        })

    except Cart.DoesNotExist:
        messages.error(request, "Your cart is empty")
        return redirect('cart')

@login_required
def order_success(request, order_id):
    order = get_object_or_404(Order, id=order_id, user=request.user)
    return render(request, 'orders/my_orders/order_success.html', {'order': order})


@login_required
def order_tracking(request):
    orders = Order.objects.filter(user=request.user).order_by('-created_at')
    return render(request, 'orders/my_orders/order_tracking.html', {'orders': orders})

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # Handle form data without saving to database
            # Example: send email instead
            return JsonResponse({
                'status': 'success',
                'message': 'Your message has been sent!'
            })
        return JsonResponse({
            'status': 'error',
            'errors': form.errors
        }, status=400)
    return JsonResponse({
        'status': 'error',
        'message': 'Invalid method'
    }, status=405)


@login_required
def profile(request):
    try:
        profile = request.user.profile
    except AttributeError:
        from .models import Profile
        profile = Profile.objects.create(user=request.user)

    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, "Profile updated successfully!")
            return redirect('profile')
    else:
        form = UserProfileForm(instance=profile)
    return render(request, 'orders/pages/profile.html', {'form': form})


@login_required
def profile_edit(request):
    if request.method == 'POST':
        form = ProfileEditForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile updated successfully!')
            return redirect('profile')
    else:
        form = ProfileEditForm(instance=request.user)

    return render(request, 'orders/pages/profile.html', {'form': form})


@login_required
def delete_account(request):
    if request.method == 'POST':
        request.user.delete()
        messages.success(request, 'Your account has been deleted.')
        return redirect('home')
    return redirect('profile')

def help(request):
    return render(request, 'orders/pages/help.html')


def signup(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = CustomUserCreationForm()

    # If form is invalid, it will show errors automatically in template
    return render(request, 'orders/pages/signup.html', {'form': form})

class MenuView(View):
    def get(self, request):
        categories = [
            ('main-dishes', 'Main Dishes'),
            ('rice-curry-comforts', 'Rice & Curry'),
            ('sandwiches-wraps', 'Sandwiches & Wraps'),
            ('sides-snacks', 'Sides & Snacks')
        ]
        return render(request, 'orders/pages/menu.html', {'categories': categories})

class DisplayMenuView(View):
    def get(self, request):
        categories = [
            ('MAIN', 'Main Dishes'),
            ('RICE', 'Rice & Curry'),
            ('SAND', 'Sandwiches & Wraps'),
            ('SIDE', 'Sides & Snacks')
        ]
        # Organize menu items by category
        menu_items_by_category = []
        for value, name in categories:
            items = MenuItem.objects.filter(category=value, available=True).order_by('name')
            menu_items_by_category.append((value, name, items))

        context = {
            'categories': [(value, name) for value, name in categories],  # For the category cards
            'menu_items_by_category': menu_items_by_category  # For the menu sections
        }
        return render(request, 'orders/pages/menu.html', context)

def privacy_policy(request):
    return render(request, 'orders/legal/privacy_policy.html')

def terms_of_service(request):
    return render(request, 'orders/legal/terms_of_service.html')

def refund_policy(request):
    return render(request, 'orders/legal/refund_policy.html')

@login_required
def complete_order(request, order_id):
    order = get_object_or_404(Order, id=order_id, user=request.user)
    if order.status != 'completed':
        order.status = 'completed'
        order.save()
    return redirect('order_tracking')

@login_required
def order_details(request, order_id):
    order = get_object_or_404(Order, id=order_id, user=request.user)
    return render(request, 'orders/order_details.html', {'order': order})