from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .models import *
from django.contrib.auth.decorators import user_passes_test, login_required
from django.http import HttpRequest
from django.shortcuts import get_object_or_404
from django import forms
from django.urls import reverse
from .forms import OrderForm, WarehouseMovementForm, BarcodeDataForm  # import form
from .models import Order, WarehouseMovement, BarcodeData      # import models
import random
import string
from django.contrib.auth.decorators import login_required


def home(request):
    testimonials_list = [
        {
            "name": "Priya Balna",
            "designation": "Senior Manager - Finance, Rapido Bike - India",
            "feedback": "We have been able to simplify our in-house inventory management with increased efficiency...",
            "image": ""  # You can add image URLs if available
        },
        {
            "name": "Shaji Anandan",
            "designation": "CMO - Promoter, Santhi UK, UK",
            "feedback": "When I thought of starting a new business initiative during the pandemic, I had no time for making business plans...",
            "image": ""
        },
        {
            "name": "Mahesh Kumar K",
            "designation": "Accounts Executive, Arthur's Food Company Pvt. Ltd., India",
            "feedback": "In the past, we tried different software applications for inventory management, but they only made the process more complicated...",
            "image": ""
        },
        {
            "name": "Jason Lee",
            "designation": "General Manager, Party Mojo Pte. Ltd., Singapore",
            "feedback": "We were introduced to Invenzo through Invenzo Books, which we've always used for our accounting needs...",
            "image": ""
        },
        {
            "name": "Atheeque Ahmed",
            "designation": "General Manager, TMM Paper Group, Bahrain",
            "feedback": "Invenzo is a very customizable software. We can make any changes in the app using the automations...",
            "image": ""
        },
        {
            "name": "Samantha Carter",
            "designation": "Head of Operations, GreenTech Solutions, Australia",
            "feedback": "Invenzo has significantly reduced our inventory discrepancies and improved our overall workflow.",
            "image": ""
        },
        {
            "name": "David Johnson",
            "designation": "CEO, Johnson Retail Group, USA",
            "feedback": "Switching to Invenzo was a game-changer for our supply chain management.",
            "image": ""
        },
        {
            "name": "Maria Gonzalez",
            "designation": "Logistics Manager, FreshMart Inc., Spain",
            "feedback": "We've seen a 35% improvement in efficiency since implementing Invenzo's automated inventory tracking.",
            "image": ""
        },
        {
            "name": "Liam O'Connor",
            "designation": "Warehouse Supervisor, Dublin Wholesale, Ireland",
            "feedback": "Managing large-scale stock has never been easier. Invenzo is truly a lifesaver!",
            "image": ""
        },
        {
            "name": "Emily Zhang",
            "designation": "Founder, EZ Beauty Products, China",
            "feedback": "With Invenzo, I can track all my stock across multiple warehouses in real-time!",
            "image": ""
        }
    ]

    return render(request, 'home.html', {'testimonials': testimonials_list})

def features(request):
    return render(request, 'features.html')

def solutions(request):
    return render(request, 'solutions.html')


def process_payment(request: HttpRequest):
    if request.method == "POST":
        plan = request.POST.get("plan")
        payment_method = request.POST.get("payment_method")

        payment_links = {
            "razorpay": "https://razorpay.com/payment-link",  # Replace with actual link
            "stripe": "https://stripe.com/pay",  # Replace with actual link
            "paypal": "https://paypal.com/payment",  # Replace with actual link
            "googlepay": "https://pay.google.com/",  # Replace with actual link
        }

        if payment_method in payment_links:
            return redirect(payment_links[payment_method])

    return redirect("payment")

# Dummy data for plans (You can fetch from the database)
plans_data = [
    {
        'id': 1,
        'name': 'Basic',
        'price': 999,
        'features': ['5 Users', '10GB Storage', 'Email Support'],
        'extras': ['Extra Storage', 'Priority Support']
    },
    {
        'id': 2,
        'name': 'Standard',
        'price': 2999,
        'features': ['50 Users', '100GB Storage', 'Premium Support'],
        'extras': ['Advanced Analytics', 'Custom Branding']
    },
    {
        'id': 3,
        'name': 'Premium',
        'price': 4999,
        'features': ['Unlimited Users', '1TB Storage', 'Dedicated Support'],
        'extras': ['AI Reports', 'Advanced Security']
    }
]

faqs = [
    {'question': 'What is Invenzo?', 'answer': 'Invenzo is an advanced inventory management system.'},
    {'question': 'Can I change my plan later?', 'answer': 'Yes, you can upgrade or downgrade anytime.'},
]

def pricing_page(request):
    return render(request, 'pricing_page.html')

@login_required
def pricing(request):
    """Render the pricing page with available plans"""
    return render(request, 'pricing.html', {'plans': plans_data, 'faqs': faqs})

@login_required
def signup_plan(request, plan_id):
    """Render the signup page for a specific plan"""
    plan = next((p for p in plans_data if p['id'] == plan_id), None)
    if not plan:
        return redirect('pricing')  # Redirect if plan ID is invalid
    return render(request, 'signup2.html', {'plan': plan})

@login_required
def payment(request):
    """Render the payment page"""
    plan_id = request.GET.get('plan')
    plan = next((p for p in plans_data if str(p['id']) == plan_id), None)
    if not plan:
        return redirect('pricing')
    return render(request, 'payment.html', {'plan': plan})


def customers(request):
    customers_list = [
        {
            "name": "Priya Balna",
            "position": "Senior Manager - Finance, Rapido Bike - India",
            "testimonial": "We have been able to simplify our in-house inventory management with increased efficiency..."
        },
        {
            "name": "Shaji Anandan",
            "position": "CMO - Promoter, Santhi UK, UK",
            "testimonial": "When I thought of starting a new business initiative during the pandemic, I had no time for making business plans..."
        },
        {
            "name": "Mahesh Kumar K",
            "position": "Accounts Executive Arthur's Food Company Pvt. Ltd., India",
            "testimonial": "In the past, we tried different software applications for inventory management, but they only made the process more complicated..."
        },
        {
            "name": "Jason Lee",
            "position": "General Manager, Party Mojo Pte. Ltd., Singapore",
            "testimonial": "We were introduced to Invenzo through Invenzo Books, which we've always used for our accounting needs..."
        },
        {
            "name": "Atheeque Ahmed",
            "position": "General Manager, TMM Paper Group, Bahrain",
            "testimonial": "Invenzo is a very customizable software. We can make any changes in the app using the automations..."
        },
        {
            "name": "Samantha Carter",
            "position": "Head of Operations, GreenTech Solutions, Australia",
            "testimonial": "Invenzo has significantly reduced our inventory discrepancies and improved our overall workflow."
        },
        {
            "name": "David Johnson",
            "position": "CEO, Johnson Retail Group, USA",
            "testimonial": "Switching to Invenzo was a game-changer for our supply chain management."
        },
        {
            "name": "Maria Gonzalez",
            "position": "Logistics Manager, FreshMart Inc., Spain",
            "testimonial": "We've seen a 35% improvement in efficiency since implementing Invenzo's automated inventory tracking."
        },
        {
            "name": "Liam O'Connor",
            "position": "Warehouse Supervisor, Dublin Wholesale, Ireland",
            "testimonial": "Managing large-scale stock has never been easier. Invenzo is truly a lifesaver!"
        },
        {
            "name": "Emily Zhang",
            "position": "Founder, EZ Beauty Products, China",
            "testimonial": "With Invenzo, I can track all my stock across multiple warehouses in real-time!"
        },
        {
            "name": "Ahmed Al-Farsi",
            "position": "Procurement Head, Gulf Electronics, UAE",
            "testimonial": "We've minimized stockouts and overstocks thanks to Invenzo's accurate demand forecasting."
        },
        {
            "name": "Jonathan Miller",
            "position": "Supply Chain Director, TechGenius, Canada",
            "testimonial": "Invenzo has transformed how we handle stock, improving our responsiveness to market demand."
        },
        {
            "name": "Fatima Hassan",
            "position": "Owner, Hassan Textiles, Pakistan",
            "testimonial": "Invenzo's intuitive interface makes inventory tracking seamless even for small businesses like ours."
        },
        {
            "name": "Ricardo Fernandes",
            "position": "Operations Lead, SuperMart Brazil, Brazil",
            "testimonial": "The automation features of Invenzo have helped us cut down on manual errors by 50%."
        },
        {
            "name": "Katarina Novak",
            "position": "Inventory Coordinator, EuroAuto Parts, Germany",
            "testimonial": "Managing automotive parts inventory is now effortless thanks to Invenzo’s robust tracking system."
        }
    ]
    return render(request, 'customers.html', {'customers': customers_list})

def integrations(request):
    return render(request, 'integrations.html')


def resources(request):
    resources_list = [
        {"icon": "📖", "title": "Help Documentation", "description": "Gain in-depth knowledge of all the features.", "link": "/help-documentation"},
        {"icon": "❓", "title": "FAQ", "description": "Find answers to common questions.", "link": "/faq"},
        {"icon": "💬", "title": "Forums", "description": "Join discussions and stay updated.", "link": "/forums"},
        {"icon": "📝", "title": "Blogs", "description": "Learn new tips and updates.", "link": "/blogs"},
        {"icon": "📊", "title": "Business Guides", "description": "Manage finances and grow successfully.", "link": "/essential-business-guides"},
        {"icon": "📅", "title": "Webinars", "description": "Join our weekly webinar sessions.", "link": "/webinar"},
    ]
    
    return render(request, 'resources.html', {'resources': resources_list})

# Inventory data
inventory_data = [
    {"name": "Retail Solutions", "url": "/solutions"},
    {"name": "Wholesale Solutions", "url": "/solutions"},
    {"name": "Pricing Plans", "url": "/pricing"},
    {"name": "Customer Stories", "url": "/customers"},
    {"name": "Integrations", "url": "/integrations"},
    {"name": "Resources & Guides", "url": "/resources"},
    {"name": "Our Team", "url": "/team"},
    {"name": "Contact Us", "url": "/contact"},
    {"name": "Webinar Registration", "url": "/webinar-registration"},
    {"name": "Item Grouping", "url": "/item-grouping"},
    {"name": "Multi-Warehouse", "url": "/multi-warehouse"},
    {"name": "Serial Tracking", "url": "/serial-tracking"},
    {"name": "Sales Order", "url": "/sales-order"},
    {"name": "Invoicing", "url": "/invoicing"},
    {"name": "Packing & Shipping", "url": "/packing-shipping"},
    {"name": "Sales Return", "url": "/sales-return"},
    {"name": "Reporting & Analytics", "url": "/reporting-analytics"},
    {"name": "SKU Generator", "url": "/sku-generator"},
    {"name": "Recorder Points", "url": "/recorder-points"},
    {"name": "Package Geometry", "url": "/package-geometry"},
    {"name": "Barcode Scanning", "url": "/barcodes"},
    {"name": "Warehouse Management", "url": "/warehouse-management"},
    {"name": "Inventory Tracking", "url": "/inventory"},
    {"name": "Order Management", "url": "/order_management"},
    {"name": "Cookies", "url": "/cookie_policy"},
    {"name": "Security", "url": "/security"},
    {"name": "Terms of Service", "url": "/terms_of_service"},
    {"name": "Reports", "url": "/reports"},
    {"name": "Privacy Policy", "url": "/privacy_policy"},
    {"name": "Login", "url": "/login"},
    {"name": "Signup", "url": "/signup"},
    {"name": "Explore", "url": "/integrations2"},
]

def search_results(request):
    query = request.GET.get('q', '').strip().lower()  # Get user input from search box

    # Filter inventory data based on the query
    filtered_results = [item for item in inventory_data if query in item["name"].lower()]

    return render(request, 'search_results.html', {'query': query, 'results': filtered_results})


# List of categories
CATEGORIES = [
    "Accessories & Jewelry", "Alcohol & Spirits", "Arts & Crafts Supplies",
    "Automotive Parts", "Baby Products", "Baking Supplies", "Beauty & Personal Care",
    "Beverages & Soft Drinks", "Books & Stationery", "Cleaning & Household Items",
    "Clothing & Apparel", "Computers & Accessories", "Construction Materials",
    "Dairy Products", "Drones & RC Vehicles", "Electrical Components",
    "Electronics", "Event & Party Supplies", "Fitness Equipment",
    "Food & Beverages", "Frozen Foods", "Furniture", "Gaming & Consoles",
    "Gardening Tools & Supplies", "Grocery & Packaged Foods",
    "Health & Wellness", "Home Appliances", "HVAC Equipment",
    "Industrial Equipment", "Kitchen Appliances", "Lighting & Fixtures",
    "Medical Supplies", "Mobile Phones & Tablets", "Music & Instruments",
    "Office Supplies", "Outdoor & Camping Gear", "Pet Supplies",
    "Pharmaceuticals", "Plumbing Supplies", "Safety & Security Equipment",
    "Shoes & Footwear", "Smart Home Devices", "Solar & Renewable Energy",
    "Sports Equipment", "Toys & Games", "Travel & Luggage",
    "Warehouse Equipment"
]
def generate_random_barcode():
    return ''.join(random.choices(string.digits, k=12))

@login_required  # Ensure the user is logged in
def order_management(request):
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            order = form.save(commit=False)  # Don't save to the database yet
            order.user = request.user  # Set the user to the currently logged-in user
            order.save()  # Now save the order
            barcode_number = generate_random_barcode()
            barcode_data = BarcodeData(
            user=request.user,
            order=order,  # ✅ This links the barcode to the order
            supplier_name=order.supplier_name,
            supplier_email=order.supplier_email,
            item_id=order.item_id,
            item_name=order.item_name,
            barcode_number=barcode_number,
            quantity=order.quantity
        )
            barcode_data.save()
            messages.success(request, 'Data added successfully!')
            return redirect('order_management')  # Redirect to the same page or another view
        else:
            print(form.errors)
    else:    
        form = OrderForm()

    return render(request, 'order_management.html', {'form': form, 'categories': CATEGORIES})


def team(request):
    return render(request, 'team.html')

@login_required  # Ensure the user is logged in
def add_warehouse_movement(request):
    if request.method == 'POST':
        form = WarehouseMovementForm(request.POST)
        if form.is_valid():
            movement = form.save(commit=False)  # Don't save to the database yet
            movement.user = request.user  # Set the user to the currently logged-in user
            movement.save()  # Now save the movement
            return redirect('warehouse_management')  # Redirect to the warehouse management page
    else:
        form = WarehouseMovementForm()

    movements = WarehouseMovement.objects.filter(user=request.user) # Fetch all movements from the database
    return render(request, 'warehouse_management.html', {'form': form, 'movements': movements})

@login_required  # Ensure the user is logged in
def update_warehouse_movement(request, movement_id):
    movement = get_object_or_404(WarehouseMovement, id=movement_id, user=request.user)  # Fetch the movement to update
    if request.method == 'POST':
        form = WarehouseMovementForm(request.POST, instance=movement)  # Bind the form to the movement instance
        if form.is_valid():
            form.save()  # Save the updated movement
            return redirect('warehouse_management')  # Redirect to the warehouse management page
    else:
        form = WarehouseMovementForm(instance=movement)  # Create a form with the existing movement data

    return render(request, 'update_movement.html', {'form': form, 'movement': movement})  # Pass the form and movement to the template

@login_required  # Ensure the user is logged in
def delete_warehouse_movement(request, movement_id):
    movement = get_object_or_404(WarehouseMovement, id=movement_id, user=request.user)  # Fetch the movement to delete
    if request.method == 'POST':
        movement.delete()  # Delete the movement
        # messages.success(request, f'Data for "{movement.movement_id}" deleted successfully!')
        return redirect('warehouse_management')  # Redirect to the warehouse management page
    return render('warehouse_management.html')  # Render a confirmation page


def superuser_check(user):
    return user.is_superuser  # Only allow superusers

@login_required
@user_passes_test(superuser_check, login_url='/error/')  # Only allow superusers
def barcode_scanning(request):
    # Fetch all barcode data since the user is an admin
    barcodes = BarcodeData.objects.all()
    return render(request, 'barcode_scanning.html', {'barcodes': barcodes})

def error_page(request):
    return render(request, 'error.html', {'message': "You don't have permission to access this page."})

def integrations2(request):
    return render(request, "integrations2.html")


@login_required  # Ensure the user is logged in
def inventory_tracking(request):
    items = Order.objects.filter(user=request.user)
    return render(request, 'inventory_tracking.html', {'items': items})

@login_required  # Ensure the user is logged in
def update_item(request, item_id):
    item = get_object_or_404(Order, id=item_id, user=request.user)  # Fetch the item to update
    if request.method == 'POST':
        form = OrderForm(request.POST, instance=item)  # Bind the form to the item instance
        if form.is_valid():
            form.save()  # Save the updated item
            return redirect('inventory_tracking')  # Redirect to the inventory tracking page
    else:
        form = OrderForm(instance=item)  # Create a form with the existing item data

    return render(request, 'update_order.html', {'form': form, 'item': item, 'categories': CATEGORIES}) 

@login_required  # Ensure the user is logged in
def delete_item(request, item_id):
    item = get_object_or_404(Order, id=item_id, user=request.user)  # Fetch the item to delete
    if request.method == 'POST':
        BarcodeData.objects.filter(item_id=item.item_id, user=request.user).delete()
        item.delete()  # Delete the item
        messages.success(request, f'Data for "{item.item_name}" deleted successfully!')
        return redirect('inventory_tracking')  # Redirect to the inventory tracking page
    return redirect('inventory_tracking.html') 

def webinar_registration(request):
    return render(request, 'webinar_registration.html')

def inventory_view(request):
    return render(request, 'inventory.html')

def item_grouping(request):
    return render(request, 'item_grouping.html')

def multi_warehouse(request):
    return render(request, 'multi_warehouse.html')

def webinar_registration(request):
    return render(request, 'webinar-registration.html')

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # Process the form data (e.g., send email or store in DB)
            form.save()  # Example, or you can email the content
            return render(request, 'contact-us.html', {'message_sent': True})
    else:
        form = ContactForm()

    return render(request, 'contact-us.html', {'form': form})

def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        user = User.objects.create_user(username=username, email=email, password=password)
        user.save()
        messages.success(request, "Registration successful!")
        return redirect('login')
    return render(request, 'register.html')

def help_documentation(request):
    return render(request, 'help-documentation.html')

def faq(request):
    return render(request, 'faq.html')

def forums(request):
    return render(request, 'forums.html')

def blogs(request):
    return render(request, 'blogs.html')

def essential_business_guides(request):
    return render(request, 'essential-business-guides.html')

def webinar(request):
    return render(request, 'webinar.html')

def reach_out_to_us(request):
    return render(request, 'reach-out-to-us.html')

def webinar(request):
    return render(request, 'webinar.html')

def save_webhook(request):
    # Your logic for handling the webhook
    return render({'status': 'success'})

def trigger_custom_function(request):
    # Your logic for triggering the custom function
    return render({'status': 'success'})

def signup_plan(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        user = User.objects.create_user(username=username, email=email, password=password)
        user.save()
        messages.success(request, "Registration successful!")
        return redirect('login')
    return render(request, 'signup2.html')

def inventory_view(request):
    return render(request, 'inventory_tracking.html') 


def update_warehouse(request):
    return render(request, 'update_warehouse.html')

def payment(request):
    plan = request.GET.get('plan', 'standard')  # Default to 'standard' if no plan is selected
    return render(request, 'payment.html', {'plan': plan})