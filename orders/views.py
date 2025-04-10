from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import CustomUserCreationForm

# This view function handles requests to the homepage of the orders app.
def index(request):
    return render(request, 'orders/index.html')

def sign_up(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()  # Save the new user
            messages.success(request, "Account created successfully! You can now log in.")
            return redirect('login')  # Redirect to login page after successful sign-up
        else:
            messages.error(request, "Please correct the errors below.")
    else:
        form = CustomUserCreationForm()
    
    return render(request, 'orders/sign_up.html', {'form': form})

# View for the login page
def login(request):
    return render(request, 'orders/login.html')

def main_dishes(request):
    dishes = [
        {"name": "Mac & Cheese (classic)", "price": 850, "image": "https://source.unsplash.com/300x200/?mac-and-cheese"},
        {"name": "Mac & Cheese (bacon/truffle/jalapeño)", "price": 1_100, "image": "https://source.unsplash.com/300x200/?mac-and-cheese-bacon"},
        {"name": "Chicken Pot Pie", "price": 1_250, "image": "https://source.unsplash.com/300x200/?chicken-pot-pie"},
        {"name": "Beef Stew", "price": 1_350, "image": "https://source.unsplash.com/300x200/?beef-stew"},
        {"name": "Shepherd’s Pie", "price": 1_200, "image": "https://source.unsplash.com/300x200/?shepherds-pie"},
        {"name": "Fried Chicken & Waffles", "price": 1_400, "image": "https://source.unsplash.com/300x200/?fried-chicken-waffles"},
        {"name": "Meatloaf with Gravy", "price": 1_300, "image": "https://source.unsplash.com/300x200/?meatloaf"},
        {"name": "Spaghetti & Meatballs", "price": 1_150, "image": "https://source.unsplash.com/300x200/?spaghetti-meatballs"},
        {"name": "Baked Ziti", "price": 1_100, "image": "https://source.unsplash.com/300x200/?baked-ziti"},
        {"name": "Stuffed Bell Peppers", "price": 1_000, "image": "https://source.unsplash.com/300x200/?stuffed-peppers"},
        {"name": "Lasagna (beef/veg/chicken)", "price": 1_250, "image": "https://source.unsplash.com/300x200/?lasagna"},
    ]
    
    return render(request, 'orders/main_dishes.html', {'dishes': dishes})

def rice_curry_comforts(request):
    rice_curry_items = [
        {'item': 'Creamy Chicken Curry with Rice', 'price': 1200},
        {'item': 'Sri Lankan Dhal Curry', 'price': 800},
        {'item': 'Coconut Milk Rice with Onion Sambal', 'price': 750},
        {'item': 'Fried Rice with Egg and Sausage', 'price': 1050},
        {'item': 'Kottu Roti (chicken/beef/egg)', 'price': '950 – 1200'}
    ]
    
    return render(request, 'orders/rice_curry_comforts.html', {'items': rice_curry_items})

def sandwiches_wraps(request):
    items = [
        {"item": "Grilled Cheese Sandwich", "price": 700, "image": "grilled_cheese_sandwich.jpg"},
        {"item": "Philly Cheesesteak", "price": 1200, "image": "philly_cheesesteak.jpg"},
        {"item": "Club Sandwich", "price": 1000, "image": "club_sandwich.jpg"},
        {"item": "Pulled Pork Sandwich", "price": 1150, "image": "pulled_pork_sandwich.jpg"},
        {"item": "Chicken Wrap with Garlic Sauce", "price": 950, "image": "chicken_wrap_with_garlic_sauce.jpg"},
        {"item": "Toasted Tuna Melt", "price": 950, "image": "toasted_tuna_melt.jpg"}
    ]
    return render(request, 'orders/sandwiches_wraps.html', {'items': items})

def sides_snacks(request):
    items = [
        {"item": "Mashed Potatoes with Gravy", "price": 500, "image": "mashed_potatoes_with_gravy.jpg"},
        {"item": "French Fries / Wedges / Curly Fries", "price": 450, "image": "french_fries.jpg"},
        {"item": "Onion Rings", "price": 500, "image": "onion_rings.jpg"},
        {"item": "Coleslaw", "price": 350, "image": "coleslaw.jpg"},
        {"item": "Buttered Corn", "price": 400, "image": "buttered_corn.jpg"},
        {"item": "Garlic Bread", "price": 450, "image": "garlic_bread.jpg"},
        {"item": "Loaded Nachos", "price": 1_100, "image": "loaded_nachos.jpg"}
    ]
    return render(request, 'orders/sides_snacks.html', {'items': items})

def menu(request):
    # Logic to render the menu page
    return render(request, 'orders/menu.html')

def about(request):
    # Logic to render the About page
    return render(request, 'orders/about.html')