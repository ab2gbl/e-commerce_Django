# E-commerce Django Backend

## Overview
This project is a backend for an e-commerce platform built with Django and Django REST Framework. It supports user management (admin/client), product catalog (phones and accessories), inventory, billing, and sales, following a modular and extensible architecture.

---

## Features
- JWT-based authentication (SimpleJWT)
- Role-based user management (Admin, Client)
- Product catalog with support for phones and accessories
- Inventory and stock management
- Billing and sales tracking
- RESTful API endpoints for all major operations
- Media upload for product images

---

## Data Models

### User
- Custom user model with roles: `ADMIN`, `CLIENT`
- Proxy models for `Admin` and `Client`

### Product
- `Product`: Base model for all products
  - Fields: `type` (phone/accessory), `brand`, `name`, `image`, `price`, `in_stock`, `available`
- `Phone`: One-to-one with `Product`, adds phone-specific fields (dimensions, weight, cpu, memory, ram, battery, camera, os, other_details)
- `Accessory`: One-to-one with `Product`, adds accessory-specific fields (dimensions, weight, other_details)

### Billing & Sales
- `Bill`: Represents a buy/sell transaction, with date, price, and products (many-to-many via `BillItem`)
- `BillItem`: Links a product to a bill with a quantity
- `Sale`: Represents a sale to a user, tracks product, quantity, date, and payment status

---

## API Endpoints

### Authentication
- `POST /users/token/` — Obtain JWT token
- `POST /users/token/refresh/` — Refresh JWT token
- `POST /users/token/verify/` — Verify JWT token

### User Management
- `POST /users/client/` — Register a new client
- `POST /users/admin/` — Register a new admin (admin only)
- `GET /users/users/` — List all users (admin only)
- `GET /users/myinfo/` — Get current user info (authenticated)

### Product Management
- `GET /product/products/` — List all products
- `POST /product/create/` — Create a new product (admin only)
- `GET /product/product/<id>` — Retrieve product details
- `PUT/PATCH/DELETE /product/editproduct/<id>` — Edit or delete a product (admin only)

### Billing
- `GET /product/bills/` — List all bills (admin only)
- `POST /product/createbills/` — Create a new bill (admin only)
- `GET /product/billitems/` — List all bill items

### Sales
- `GET/POST /product/sales/` — List or create sales

---

## APIs

This section explains the main API groups, their purposes, and usage examples.

### 1. Authentication APIs
These endpoints handle user authentication using JWT tokens.

- **Obtain Token**
  - `POST /users/token/`
  - **Request:**
    ```json
    { "username": "your_username", "password": "your_password" }
    ```
  - **Response:**
    ```json
    { "refresh": "<refresh_token>", "access": "<access_token>" }
    ```
- **Refresh Token**
  - `POST /users/token/refresh/`
  - **Request:**
    ```json
    { "refresh": "<refresh_token>" }
    ```
  - **Response:**
    ```json
    { "access": "<new_access_token>" }
    ```
- **Verify Token**
  - `POST /users/token/verify/`
  - **Request:**
    ```json
    { "token": "<access_token>" }
    ```

### 2. User Management APIs
Manage user registration, listing, and profile retrieval.

- **Register Client**
  - `POST /users/client/`
  - **Request:**
    ```json
    { "username": "client1", "email": "client1@email.com", "password": "your_password" }
    ```
- **Register Admin** (admin only)
  - `POST /users/admin/`
  - **Request:**
    ```json
    { "username": "admin1", "email": "admin@email.com", "password": "your_password" }
    ```
- **List Users** (admin only)
  - `GET /users/users/`
- **Get My Info**
  - `GET /users/myinfo/` (requires authentication)

### 3. Product Management APIs
Manage products, including creation, listing, and editing.

- **List Products**
  - `GET /product/products/`
- **Create Product** (admin only)
  - `POST /product/create/`
  - **Request Example (Phone):**
    ```json
    {
      "type": "phone",
      "brand": "Samsung",
      "name": "Galaxy S23 Ultra",
      "image": "<image_file>",
      "price": "1200.000",
      "dimensions": "163.4 x 78.1 x 8.9 mm",
      "weight": "234g",
      "cpu": "Snapdragon 8 Gen 2",
      "memory": "256GB",
      "ram": "8GB",
      "battery": "5000mAh",
      "camera": "200MP",
      "os": "Android 13",
      "other_details": "5G support"
    }
    ```
- **Get Product Details**
  - `GET /product/product/<id>`
- **Edit/Delete Product** (admin only)
  - `PUT/PATCH/DELETE /product/editproduct/<id>`

### 4. Billing APIs
Track product purchases and sales via bills.

- **List Bills** (admin only)
  - `GET /product/bills/`
- **Create Bill** (admin only)
  - `POST /product/createbills/`
  - **Request Example:**
    ```json
    {
      "type": "buy",
      "date": "2024-06-09",
      "products": [
        { "product": 5, "quantity": 2 }
      ],
      "price": 1000
    }
    ```
- **List Bill Items**
  - `GET /product/billitems/`

### 5. Sales APIs
Track and create sales transactions.

- **List Sales**
  - `GET /product/sales/`
- **Create Sale**
  - `POST /product/sales/`
  - **Request Example:**
    ```json
    {
      "user": 1,
      "product": 2,
      "quantity": 1,
      "date": "2024-06-10"
    }
    ```

**Note:** For all protected endpoints, include the JWT access token in the `Authorization` header:
```
Authorization: Bearer <your-access-token>
```

---

## Setup Instructions

1. **Clone the repository**
   ```bash
   git clone <repo-url>
   cd ecommerce
   ```
2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```
3. **Apply migrations**
   ```bash
   python manage.py migrate
   ```
4. **Create a superuser**
   ```bash
   python manage.py createsuperuser
   ```
5. **Run the development server**
   ```bash
   python manage.py runserver
   ```
6. **Access the admin panel**
   - Visit `http://127.0.0.1:8000/admin/`

---

## Media & Static Files
- Product images are uploaded to `media/upload/products/`.
- Configure `MEDIA_URL` and `MEDIA_ROOT` in `settings.py` as needed.

---

## Authentication
- Uses JWT (JSON Web Tokens) via `djangorestframework-simplejwt`.
- Include the access token in the `Authorization` header for protected endpoints:
  ```
  Authorization: Bearer <your-access-token>
  ```

---

## Dependencies
Key dependencies (see `requirements.txt` for full list):
- Django==5.0.4
- djangorestframework==3.14.0
- djangorestframework-simplejwt
- django-cors-headers
- pillow

---

## Project Structure
- `ecommerce/` — Project settings and root URLs
- `product/` — Product, billing, and sales models, views, serializers, and URLs
- `users/` — Custom user model, authentication, views, serializers, and URLs
- `media/` — Uploaded product images

---

## Notes
- The backend is designed to be used with a frontend client (not included).
- For API testing, use tools like Postman or HTTPie.
- For further customization, see the code and comments in each app.
