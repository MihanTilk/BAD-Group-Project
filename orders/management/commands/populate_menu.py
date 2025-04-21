from django.core.management.base import BaseCommand
from orders.models import MenuItem

class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        # Clear existing items
        MenuItem.objects.all().delete()
        self.stdout.write(self.style.WARNING('Deleted all existing menu items'))

        menu_items_data = [
            {
                'name': 'Baked Ziti',
                'description': 'Classic Italian pasta bake with rich tomato sauce and melted cheese',
                'price': 1450.00,
                'category': 'MAIN',
                'image': 'images/Baked_Ziti.jpg',
                'is_special': True
            },
            {
                'name': 'Beef Stew',
                'description': 'Hearty beef stew with root vegetables in red wine sauce',
                'price': 1650.00,
                'category': 'MAIN',
                'image': 'images/Beef_Stew.jpg'
            },
            {
                'name': 'Buttered Corn',
                'description': 'Sweet corn kernels tossed in creamy butter',
                'price': 450.00,
                'category': 'SIDE',
                'image': 'images/Buttered_Corn.jpg'
            },
            {
                'name': 'Chicken Pot Pie',
                'description': 'Classic comfort food with flaky pastry crust',
                'price': 1350.00,
                'category': 'MAIN',
                'image': 'images/Chicken_Pot_Pie.jpg'
            },
            {
                'name': 'Chicken Wrap with Garlic Sauce',
                'description': 'Grilled chicken wrap with fresh vegetables and garlic aioli',
                'price': 950.00,
                'category': 'SAND',
                'image': 'images/Chicken_Wrap_with_Garlic_Sauce.jpg'
            },
            {
                'name': 'Club Sandwich',
                'description': 'Triple-decker sandwich with turkey, bacon, lettuce and tomato',
                'price': 1250.00,
                'category': 'SAND',
                'image': 'images/Club_Sandwich.jpg'
            },
            # Rice & Curry (RICE)
            {
                'name': 'Coconut Milk Rice with Onion Sambal',
                'description': 'Fragrant coconut rice served with traditional onion sambal',
                'price': 950.00,
                'category': 'RICE',
                'image': 'images/Coconut_Milk_Rice_with_Onion_Sambal.jpg',
                'is_special': True
            },
            {
                'name': 'Coleslaw',
                'description': 'Crispy cabbage and carrot salad with creamy dressing',
                'price': 400.00,
                'category': 'SIDE',
                'image': 'images/Coleslaw.jpg'
            },
            {
                'name': 'Creamy Chicken Curry with Rice',
                'description': 'Sri Lankan-style chicken curry with steamed rice',
                'price': 1450.00,
                'category': 'RICE',
                'image': 'images/Creamy_Chicken_Curry_with_Rice.jpg',
                'is_special': True
            },
            {
                'name': 'Creamy Chicken Pot Pie',
                'description': 'Rich and creamy chicken pot pie with flaky crust',
                'price': 1450.00,
                'category': 'MAIN',
                'image': 'images/Creamy_Chicken_Pot_Pie.jpg'
            },
            # Sides (SIDE)
            {
                'name': 'French Fries',
                'description': 'Crispy golden fries served with ketchup',
                'price': 450.00,
                'category': 'SIDE',
                'image': 'images/French_Fries.jpg'
            },
            {
                'name': 'Fried Chicken and Waffles',
                'description': 'Southern-style crispy chicken with maple syrup waffles',
                'price': 1650.00,
                'category': 'MAIN',
                'image': 'images/Fried_Chicken_and_Waffles.jpg'
            },
            {
                'name': 'Fried Rice with Egg and Sausage',
                'description': 'Wok-fried rice with egg, sausage and vegetables',
                'price': 1250.00,
                'category': 'MAIN',
                'image': 'images/Fried_Rice_with_Egg_and_Sausage.jpg'
            },
            {
                'name': 'Garlic Bread',
                'description': 'Toasted bread with garlic butter and herbs',
                'price': 400.00,
                'category': 'SIDE',
                'image': 'images/Garlic_Bread.jpg'
            },
            # Sandwiches (SAND)
            {
                'name': 'Gourmet Burger',
                'description': 'Premium beef patty with cheese and special sauce',
                'price': 1550.00,
                'category': 'SAND',
                'image': 'images/Gourmet_Burger.jpg',
                'is_special': True
            },
            {
                'name': 'Grilled Cheese Sandwich',
                'description': 'Golden toasted sandwich with three cheese blend',
                'price': 850.00,
                'category': 'SAND',
                'image': 'images/Grilled_Cheese_Sandwich.jpg'
            },
            {
                'name': 'Kottu Roti',
                'description': 'Sri Lankan chopped roti with vegetables and meat',
                'price': 1350.00,
                'category': 'MAIN',
                'image': 'images/Kottu_Roti.jpg',
                'is_special': True
            },
            {
                'name': 'Lasagna',
                'description': 'Layered pasta with meat sauce and cheese',
                'price': 1450.00,
                'category': 'MAIN',
                'image': 'images/Lasagna.jpg'
            },
            {
                'name': 'Loaded Nachos',
                'description': 'Crispy tortilla chips with cheese, salsa and guacamole',
                'price': 950.00,
                'category': 'SIDE',
                'image': 'images/Loaded_Nachos.jpg'
            },
            {
                'name': 'Mac and Cheese Bacon',
                'description': 'Creamy macaroni cheese with crispy bacon bits',
                'price': 1250.00,
                'category': 'SIDE',
                'image': 'images/Mac_and_Cheese_Bacon.jpg'
            },
            {
                'name': 'Mac and Cheese Classic',
                'description': 'Traditional creamy macaroni and cheese',
                'price': 1150.00,
                'category': 'SIDE',
                'image': 'images/Mac_and_Cheese_Classic.jpg'
            },
            {
                'name': 'Mashed Potatoes with Gravy',
                'description': 'Creamy mashed potatoes with rich beef gravy',
                'price': 550.00,
                'category': 'SIDE',
                'image': 'images/Mashed_Potatoes_with_Gravy.jpg'
            },
            {
                'name': 'Meatloaf with Gravy',
                'description': 'Homestyle meatloaf with mushroom gravy',
                'price': 1450.00,
                'category': 'MAIN',
                'image': 'images/Meatloaf_with_Gravy.jpg'
            },
            {
                'name': 'Onion Rings',
                'description': 'Crispy beer-battered onion rings',
                'price': 650.00,
                'category': 'SIDE',
                'image': 'images/Onion_Rings.jpg'
            },
            {
                'name': 'Pasta Carbonara',
                'description': 'Classic Italian pasta with egg and pancetta',
                'price': 1550.00,
                'category': 'MAIN',
                'image': 'images/Pasta_Carbonara.jpg'
            },
            {
                'name': 'Philly Cheesesteak',
                'description': 'Sliced steak with melted cheese and caramelized onions',
                'price': 1650.00,
                'category': 'SAND',
                'image': 'images/Philly_Cheesesteak.jpg'
            },
            {
                'name': 'Pulled Pork Sandwich',
                'description': 'Slow-cooked pork shoulder with BBQ sauce',
                'price': 1450.00,
                'category': 'SAND',
                'image': 'images/Pulled_Pork_Sandwich.jpg'
            },
            {
                'name': "Shepherd's Pie",
                'description': 'Ground meat pie with mashed potato topping',
                'price': 1350.00,
                'category': 'MAIN',
                'image': 'images/Shepherds_Pie.jpg'
            },
            {
                'name': 'Spaghetti and Meatballs',
                'description': 'Classic spaghetti with homemade meatballs',
                'price': 1450.00,
                'category': 'MAIN',
                'image': 'images/Spaghetti_and_Meatballs.jpg'
            },
            {
                'name': 'Sri Lankan Dhal Curry',
                'description': 'Traditional lentil curry with coconut milk',
                'price': 850.00,
                'category': 'RICE',
                'image': 'images/Sri_Lankan_Dhal_Curry.jpg'
            },
            {
                'name': 'Stuffed Bell Peppers',
                'description': 'Bell peppers stuffed with rice and minced meat',
                'price': 1250.00,
                'category': 'MAIN',
                'image': 'images/Stuffed_Bell_Peppers.jpg'
            },
            {
                'name': 'Toasted Tuna Melt',
                'description': 'Tuna salad melt with melted cheddar cheese',
                'price': 1150.00,
                'category': 'SAND',
                'image': 'images/Toasted_Tuna_Melt.jpg'
            },
        ]

        # Create menu items
        for item_data in menu_items_data:
            MenuItem.objects.create(
                name=item_data['name'],
                description=item_data['description'],
                price=item_data['price'],
                category=item_data['category'],
                image=item_data['image'],
                is_special=item_data.get('is_special', False),
                available=True
            )

        self.stdout.write(self.style.SUCCESS(f'Successfully created {len(menu_items_data)} menu items!'))

# To run this command, use the following command in your terminal:
#python manage.py populate_menu