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
from django.core.mail import send_mail, mail_admins
from django.conf import settings
from django.shortcuts import render, redirect
from .forms import ContactForm
from .models import ContactMessage

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
        cart_items = cart.items.all()
        total = sum(item.total_price for item in cart_items)
        # Store cart count in session
        request.session['cart_count'] = cart.items.count()
    except Cart.DoesNotExist:
        cart_items = None
        total = 0
        request.session['cart_count'] = 0

    return render(request, 'orders/pages/cart.html', {
        'cart_items': cart_items,
        'total_cost': total,
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
            cart_count = cart.items.count()
            request.session['cart_count'] = cart_count  # Store in session
            return JsonResponse({
                'success': True,
                'message': f"{menu_item.name} added to cart!",
                'cart_count': cart_count,
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

        # Get cart count before clearing
        cart_count = cart.items.count()

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

            # Clear the cart after successful order creation
            cart.items.all().delete()

            # Set session cart count to 0
            request.session['cart_count'] = 0

            # Redirect to success page with order ID
            return redirect('order_success', order_id=order.id)
        else:
            messages.error(request, "Your cart is empty")
            return redirect('cart')

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

def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # Save the message to database
            contact_message = form.save()
            
            # Send email to admin
            mail_admins(
                subject=f"New Contact Message from {contact_message.name}",
                message=f"Name: {contact_message.name}\nEmail: {contact_message.email}\n\nMessage:\n{contact_message.message}",
                fail_silently=False,
            )
            
            # Send confirmation email to user
            send_mail(
                subject="Your message has been received",
                message=f"Dear {contact_message.name},\n\nThank you for contacting us. We have received your message and will get back to you soon.\n\nYour message:\n{contact_message.message}\n\nBest regards,\nThe Warm & Whisked Team",
                from_email=settings.DEFAULT_FROM_EMAIL,
                recipient_list=[contact_message.email],
                fail_silently=False,
            )
            
            messages.success(request, 'Your message has been sent successfully!')
            return redirect(request.META.get('HTTP_REFERER', 'home'))
    else:
        form = ContactForm()
    
    return render(request, 'orders/pages/contact.html', {'form': form})


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
        # Define categories
        categories = [
            ('MAIN', 'Main Dishes'),
            ('RICE', 'Rice & Curry'),
            ('SAND', 'Sandwiches & Wraps'),
            ('SIDE', 'Sides & Snacks')
        ]
        
        # Get filter parameters from request
        meat_filter = request.GET.get('meat', None)
        category_filter = request.GET.get('category', None)
        price_sort = request.GET.get('price_sort', None)
        
        # Base queryset
        menu_items = MenuItem.objects.filter(available=True)
        
        # Apply filters if they exist
        if meat_filter:
            menu_items = menu_items.filter(meat_category=meat_filter)
        if category_filter:
            menu_items = menu_items.filter(category=category_filter)

        # Apply sorting if specified
        if price_sort == 'asc':
            menu_items = menu_items.order_by('price')
        elif price_sort == 'desc':
            menu_items = menu_items.order_by('-price')

        # Organize menu items by category
        menu_items_by_category = []
        for value, name in categories:
            items = menu_items.filter(category=value)
            if items.exists():  # Only add categories that have items
                menu_items_by_category.append((value, name, items))

        context = {
            'categories': [(value, name) for value, name in categories],
            'menu_items_by_category': menu_items_by_category,
            'meat_categories': MenuItem.MEAT_CHOICES,
            'current_meat_filter': meat_filter,
            'current_category_filter': category_filter,
            'current_price_sort': price_sort  # <-- Add this line
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