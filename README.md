# Book Store API

A simple Django REST Framework API for a book store with user authentication, book management, shopping cart, and reviews.

## ✨ Features

- User registration and login with JWT
- Create, read, update, delete books
- Manage authors and categories
- Filter books by title, category, and price
- Shopping cart (add/remove items)
- Rate and review books
- User profiles

## 🛠️ Tech Stack

- Django 6.0.3
- Django REST Framework 3.16.1
- JWT Authentication (djangorestframework-simplejwt)
- SQLite (development)
- Pillow (image processing)

## 📥 Installation

### Requirements
- Python 3.9+
- pip

### Setup Steps

1. Clone the repository:
```bash
git clone https://github.com/AhmedEl-Khouly/Book-Store-API.git
cd Book-Store-API
```

2. Create virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Run migrations:
```bash
python manage.py migrate
```

5. Create admin user:
```bash
python manage.py createsuperuser
```

6. Start the server:
```bash
python manage.py runserver
```

Access the API at: `http://localhost:8000/api/`

## 📡 API Endpoints

### User Endpoints
| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | `/api/register/` | Register new user |
| POST | `/api/token/` | Get access token |
| GET | `/api/profile/` | Get user profile |

### Book Endpoints
| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/api/books/` | List all books |
| GET | `/api/books/<id>/` | Get book details |
| POST | `/api/books/create/` | Create book (admin only) |
| PUT | `/api/books/<id>/update/delete/` | Update book (admin) |
| DELETE | `/api/books/<id>/update/delete/` | Delete book (admin) |

### Author Endpoints
| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/api/authors/` | List all authors |
| GET | `/api/authors/<id>/` | Get author details |
| POST | `/api/authors/` | Create author (admin) |

### Category Endpoints
| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/api/categories/` | List all categories |
| GET | `/api/categories/<slug>/` | Get category by slug |
| POST | `/api/categories/create/` | Create category (admin) |

### Cart Endpoints
| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/api/cart/` | Get user's cart |
| POST | `/api/cartitem/` | Add item to cart |
| DELETE | `/api/cartitem/<id>/` | Remove from cart |

### Review Endpoints
| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/api/books/<book_id>/reviews/` | Get book reviews |
| POST | `/api/books/<book_id>/reviews/` | Create review |

## 🔐 Authentication

The API uses JWT (JSON Web Tokens):

1. Register and get credentials
2. Login with username/password at `/api/token/` to get access token
3. Use token in request header: `Authorization: Bearer <your_token>`
4. Access token expires after 30 minutes
5. Refresh token with `/api/token/refresh/`

## 👤 Author

Ahmed El-Khouly
