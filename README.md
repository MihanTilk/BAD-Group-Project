Restaurant Ordering System -  Group 7

Group Members:
FERNANDO D.S.R.  226030K
LIYANAGE T.S.    226075C
TILAKARATNE M.D. 226121P

A Django-based web application for a fictional restaurant, Warm & Whisked, that allows customers to browse a menu, filter and sort items, add to cart, like dishes, and place orders through an intuitive and responsive user interface.

🌟 Features
* User registration, login, and logout
* Dynamic homepage with today’s specials and customer reviews
* Menu with filtering by protein (VEG, CHK, BEEF, PRK, FIS) and dish type (MAIN, RICE, SAND, SIDE)
* Sort menu items by price or popularity
* Like functionality for menu items
* Add to cart, update quantities, delete individual items or clear entire cart
* Checkout process with order confirmation and order cancellation
* Most liked items display
* Reusable base.html for layout uniformity (header and footer rendering)
* Admin panel to manage menu items, profiles, and orders

🌐 Technical Details
Backend: Python, Django
Frontend: HTML, Bootstrap 5, JavaScript
Database: SQLite (default)

💡 Usage Instructions
* Register a new account or login to access cart and order features
* Browse menu and apply filters/sorting
* Click "Like" to like menu items
* Add items to cart, update quantities, or delete them
* View cart from the navbar icon or cart page
* Proceed to checkout to confirm your order and clear the cart
* Complete order when received or cancel order within 5 minutes
* Use the admin panel (/admin) to manage menu items and users (for authorized users)

_(Note: populate_menu.py was initially used to add many menu items to the database at once through python code, but is not required for normal operation. The menu can be managed through the admin panel.)_

🚀 Installation and Setup
Clone the Repository
Set Up a Virtual Environment
Install Dependencies (pip install -r requirements.txt)
Apply Migrations (python manage.py migrate)
Run the Development Server (python manage.py runserver)

🌟 Future Enhancements
Add payment gateway integration for online payments.

User Interface Wireframe (created using Figma):
Home Page:
![Home_Page_Wireframe1.png](..%2F..%2F..%2FDownloads%2FHome_Page_Wireframe1.png)

Menu Page:
![Menu_Page_Wireframe2.png](..%2F..%2F..%2FDownloads%2FMenu_Page_Wireframe2.png)

Cart Page:
![Cart_Page_Wireframe3.png](..%2F..%2F..%2FDownloads%2FCart_Page_Wireframe3.png)

Help Page:
![Help_Page_Wireframe4.png](..%2F..%2F..%2FDownloads%2FHelp_Page_Wireframe4.png)

Profile Page:
![Profile_Page_Wireframe5.png](..%2F..%2F..%2FDownloads%2FProfile_Page_Wireframe5.png)

My Orders Page:
![My_Orders_Page_Wireframe6.png](..%2F..%2F..%2FDownloads%2FMy_Orders_Page_Wireframe6.png)
