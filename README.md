
E-Juice Sharing Platform
This project is a Django-based e-commerce platform designed to facilitate the sharing of e-juice bottles for electronic cigarettes. Users can browse products, view detailed descriptions, and order e-juice in shared slots.

Features
Product Management: Admins can add, edit, and delete products with detailed descriptions and images.
Category Management: Organize products into categories.
Customer Management: Register and manage customer profiles.
Order Management: Allow customers to order e-juice in shared slots based on bottle size.
API Endpoints: RESTful API for product, category, and order management.
Installation
Clone the Repository

bash
Copy code
git clone https://github.com/yourusername/e-juice-platform.git
cd e-juice-platform
Create and Activate a Virtual Environment

bash
Copy code
python -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
Install Dependencies

bash
Copy code
pip install -r requirements.txt
Run Migrations

bash
Copy code
python manage.py makemigrations
python manage.py migrate
Create a Superuser

bash
Copy code
python manage.py createsuperuser
Run the Development Server

bash
Copy code
python manage.py runserver
Access the Admin Panel

Open your browser and go to http://127.0.0.1:8000/admin to log in with your superuser credentials.

Project Structure
ejuice_platform/: Project settings and configuration files.
shop/: Django app containing models, views, serializers, and URLs for product management.
Models
Product: Stores details of each product including title, short and long descriptions, category, price, image, and unit size.
Category: Represents categories to organize products.
Customer: Stores customer profile information linked to the Django User model.
Order: Manages orders by customers, ensuring that the number of slots ordered does not exceed available slots.
API Endpoints
Products: /api/products/

GET: List all products
POST: Create a new product
GET /{id}/: Retrieve a specific product
PUT /{id}/: Update a product
DELETE /{id}/: Delete a product
Categories: /api/categories/

GET: List all categories
POST: Create a new category
GET /{id}/: Retrieve a specific category
PUT /{id}/: Update a category
DELETE /{id}/: Delete a category
Orders: /api/orders/

GET: List all orders
POST: Create a new order
GET /{id}/: Retrieve a specific order
PUT /{id}/: Update an order
DELETE /{id}/: Delete an order
Future Enhancements
User Authentication: Secure API endpoints using JWT or session-based authentication.
Frontend Integration: Develop a frontend using React or React Native to interact with the Django backend.
Payment Integration: Integrate payment gateways like Stripe or PayPal.
Testing: Write unit and integration tests to ensure reliability.
Contributing
Fork the repository.
Create a new branch for your feature or bug fix.
Commit your changes and push your branch to GitHub.
Open a pull request with a description of your changes.
License
This project is licensed under the MIT License. See the LICENSE file for more details.
