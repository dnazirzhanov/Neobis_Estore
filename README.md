# Estore Project

## Description
Estore is a Django Rest Framework (DRF) project for managing an online store. It provides APIs for user registration, authentication, product management, and order processing.

## Features
- User registration and authentication
- Product management (CRUD operations)
- Order processing
- Token-based authentication using DRF's Token Authentication

## Technologies Used
- Django: a high-level Python web framework
- Django Rest Framework (DRF): a powerful toolkit for building Web APIs in Django
- SQLite: a lightweight relational database used for development
- Git: a version control system for tracking changes in the project
- GitHub: a platform for hosting Git repositories and collaborating with others


### Installation

1. Clone the repository:

    ```bash
    git clone [https://github.com/dnazirzhanov/Neobis_DjangoGirls.git](https://github.com/dnazirzhanov/Neobis_Estore.git)
    ```

2. Navigate to the project directory:

    ```bash
    cd e_store
    ```

3. Create a virtual environment (optional but recommended):

    ```bash
    python -m venv venv
    ```

4. Activate the virtual environment:

    - On Windows:

        ```bash
        .\venv\Scripts\activate
        ```

    - On macOS/Linux:

        ```bash
        source venv/bin/activate
        ```

5. Install dependencies:

    ```bash
    pip install -r requirements.txt
    ```


6. Apply database migrations:

    ```bash
    python manage.py migrate
    ```

7. Run the development server:

    ```bash
    python manage.py runserver
    ```

8. Access the API at http://127.0.0.1:8000/api/

### API Endpoints:

* POST /api/register/: User registration
* POST /api/login/: User login (returns authentication token)
* POST /api/logout/: User logout
* GET /api/products/: List all products
* POST /api/products/: Create a new product
* GET /api/products/{id}/: Retrieve a product by ID
* GET /api/orders/: List all orders
* POST /api/orders/: Create a new order


