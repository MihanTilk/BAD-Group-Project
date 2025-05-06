Restaurant Ordering System Grp 7

A Django-based web application for a fictional restaurant, Warm & Whisked, that allows customers to browse a menu, filter and sort items, add to cart, like dishes, and place orders through an intuitive and responsive user interface.

🌟 Features
User registration, login, and logout
Dynamic homepage with today’s specials and customer reviews
Menu with filtering by protein (e.g., VEG, CHK, BEEF) and dish type
Sort menu items by price or popularity
Like functionality for menu items
Add to cart, update quantities, delete individual items or clear entire cart
Checkout process with order confirmation
Most liked items display
Reusable base.html for layout uniformity (header and footer rendering)
Admin panel to manage menu items, profiles, and orders

🌐 Technical Details
Backend: Python, Django
Frontend: HTML, Bootstrap 5, JavaScript
Database: SQLite (default)

💡 Usage Instructions
Register a new account or login to access cart and order features
Browse menu and apply filters/sorting
Click "Like" to like menu items
Add items to cart, update quantities, or delete them
View cart from the navbar icon or cart page
Proceed to checkout to confirm your order and clear the cart
Use the admin panel (/admin) to manage menu items and users


🚀 Installation and Setup
Clone the Repository
Set Up a Virtual Environment
Install Dependencies (pip install -r requirements.txt)
Apply Migrations (python manage.py migrate)
Run the Development Server (python manage.py runserver)

🌟 Future Enhancements
Add payment gateway integration for online payments.
