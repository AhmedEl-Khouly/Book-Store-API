# Book-Store-API

## Introduction
This project is an API for managing a Book Store. The goal of the project is to provide services such as managing books, authors, categories, carts, reviews, and users.

## Main Directories

- **authors/**: Contains the management of authors, including models, views, and URLs.
- **books/**: Contains the management of books, including filters, models, views, and URLs.
- **cart/**: Contains the management of carts, including models, views, and URLs.
- **categories/**: Contains the management of categories, including models, views, and URLs.
- **reviews/**: Contains the management of reviews, including models, permissions, views, and URLs.
- **users/**: Contains the management of users, including models, signals, views, and URLs.
- **bookstore/**: Contains the main project settings such as Django settings, ASGI, and WSGI files.

## Database
- SQLite is used as the default database.
- The database includes tables for managing books, authors, categories, users, reviews, and carts.

## Media
- Images are stored in the `media/` folder:
  - `authors-images/`: For storing author images.
  - `books-images/`: For storing book images.

## Current Features
- Author management (add, edit, delete).
- Book management (add, edit, delete).
- Category management.
- User management.
- Review management.
- Cart management.

## Requirements
To run the project, ensure the following requirements are installed:

- Python 3.9 or later.
- Python libraries listed in the `requirements.txt` file.

## How to Run
1. Install the requirements:
   ```bash
   pip install -r requirements.txt
   ```
2. Apply migrations:
   ```bash
   python manage.py migrate
   ```
3. Run the local server:
   ```bash
   python manage.py runserver
   ```

## Contributors
- The development team responsible for the project.

## Additional Notes
- Migrations are stored in the `migrations/` folder for each app.
- The project uses Django as the main framework.