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
![Home_Page_Wireframe1](https://github.com/user-attachments/assets/7edb0c27-6cdd-4e6c-a027-7d21a373a339)

Menu Page:
![Menu_Page_Wireframe2](https://github.com/user-attachments/assets/ba730628-a81d-43b0-a4d5-2881be68de2c)

Cart Page:
![Cart_Page_Wireframe3](https://github.com/user-attachments/assets/062a0dbd-6754-4519-b61b-a01ddc617bc2)

Help Page:
![Help_Page_Wireframe4](https://github.com/user-attachments/assets/35308048-6ab5-476c-a8e2-09da7baa5a6e)

Profile Page:
![Profile_Page_Wireframe5](https://github.com/user-attachments/assets/04704dd4-5261-4606-abbd-3636323e6618)

My Orders Page:
![My_Orders_Page_Wireframe6](https://github.com/user-attachments/assets/a6476461-df78-4d97-bb5e-0158af99df8f)
