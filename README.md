# 🛍️ ShopEase - E-Commerce Store

ShopEase is a full-stack e-commerce web application developed as part of a Full Stack Development Internship Task.

The application allows users to browse products, view product details, add products to a shopping cart, place orders, and view their order history.

---

## 🚀 Features

- 👤 User Registration
- 🔐 User Login and Logout
- 🛍️ Product Listing
- 🔎 Product Details
- 🖼️ Product Images
- 🛒 Shopping Cart
- ➕ Increase Product Quantity
- ➖ Decrease Product Quantity
- ❌ Remove Products from Cart
- 📦 Stock Management
- 💳 Checkout System
- 🧾 Order Processing
- 📋 Order History
- 👨‍💼 Django Admin Panel
- 📱 Responsive Design
- ✨ Animated User Interface

---

## 🛠️ Technologies Used

- **Frontend:** HTML5, CSS3, JavaScript
- **Backend:** Python, Django
- **Database:** SQLite
- **Image Handling:** Pillow
- **Version Control:** Git & GitHub

---

## 📂 Project Structure

```text
codealpha-ecommerce/
│
├── ecommerce/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
│
├── store/
│   ├── migrations/
│   ├── templates/
│   │   └── store/
│   │       ├── product_list.html
│   │       ├── product_detail.html
│   │       ├── cart.html
│   │       ├── login.html
│   │       ├── register.html
│   │       ├── checkout.html
│   │       ├── order_success.html
│   │       └── order_history.html
│   │
│   ├── static/
│   │   └── store/
│   │       └── style.css
│   │
│   ├── admin.py
│   ├── models.py
│   ├── urls.py
│   └── views.py
│
├── manage.py
├── requirements.txt
├── .gitignore
└── README.md
```

---

## ⚙️ Installation and Setup

### 1. Clone the Repository

```bash
git clone https://github.com/ilapandaranjitha2007-python/ecommerce-store.git
```

### 2. Open the Project Folder

```bash
cd ecommerce-store
```

### 3. Create a Virtual Environment

```bash
python -m venv venv
```

### 4. Activate the Virtual Environment

For Windows PowerShell:

```powershell
venv\Scripts\Activate.ps1
```

If PowerShell shows an execution-policy error:

```powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy RemoteSigned
```

Then activate the virtual environment:

```powershell
venv\Scripts\Activate.ps1
```

### 5. Install Required Packages

```bash
pip install -r requirements.txt
```

### 6. Apply Database Migrations

```bash
python manage.py migrate
```

### 7. Create an Admin Account

```bash
python manage.py createsuperuser
```

### 8. Run the Development Server

```bash
python manage.py runserver
```

Open the application in your browser:

```text
http://127.0.0.1:8000/
```

---

## 👨‍💼 Admin Panel

The Django admin panel can be accessed at:

```text
http://127.0.0.1:8000/admin/
```

The administrator can manage:

- Products
- Orders
- Order Items
- Users

---

## 🛒 How the Application Works

### 1. Home Page

Users can view the available products along with their prices, descriptions, images, and stock information.

### 2. Product Details

Users can select a product to view its complete details.

### 3. Shopping Cart

Users can:

- Add products
- Increase quantity
- Decrease quantity
- Remove products
- View the total amount

### 4. Checkout

Logged-in users can enter:

- Full Name
- Delivery Address
- Phone Number

and place an order.

### 5. Order Processing

After an order is placed:

- The order is saved in the database.
- Order items are created.
- Product stock is reduced.
- The shopping cart is cleared.

### 6. Order History

Logged-in users can view their previous orders and order details.

---

## 🗄️ Database Models

The application uses the following main models.

### Product

Stores:

- Product Name
- Description
- Price
- Stock
- Product Image
- Created Date

### Order

Stores:

- User
- Customer Name
- Address
- Phone Number
- Total Amount
- Order Date

### OrderItem

Stores:

- Order
- Product
- Quantity
- Product Price

---

## 🔐 Authentication

The application provides:

- User Registration
- User Login
- User Logout
- Authentication before checkout
- User-specific order history

---

## 📱 Responsive Design

The application is designed to work on:

- Desktop
- Laptop
- Tablet
- Mobile devices

---

## 🧪 Project Testing

The following functionality has been tested:

- User registration
- User login
- Product listing
- Product details
- Add to cart
- Increase quantity
- Decrease quantity
- Remove from cart
- Checkout
- Order creation
- Stock reduction
- Order history
- User logout

---

## 📌 Project Information

**Project Name:** ShopEase - E-Commerce Store

**Project Type:** Full Stack Development Internship Task

**Backend:** Django

**Database:** SQLite

**Frontend:** HTML, CSS, JavaScript

**Image Handling:** Pillow

**Version Control:** Git & GitHub

---

## 👨‍💻 Author

**Ranjitha Ilapanda**

---

## 📄 License

This project was developed for educational and internship purposes.