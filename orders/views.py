from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import CustomUserCreationForm

# This view function handles requests to the homepage of the orders app.
def index(request):
    # It renders and returns the 'index.html' template from 'orders/templates/orders/'
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
    # Define a list of items with names, prices, and image URLs
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
    
    # Pass the dishes to the template
    return render(request, 'orders/main_dishes.html', {'dishes': dishes})
