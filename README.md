# 📝 Bloggy — A Simple Blog Platform Built with Django

A simple blog built with Django to practice core concepts:
- CRUD operations (Create, Read, Update, Delete) for posts
- Django ORM and MVT architecture
- User authentication (Signup, Login, Logout)
- Modern, responsive UI with dark theme

## Features
- Add, view, edit, and delete posts
- Image banner support for posts (MEDIA configured)
- User registration, login, and logout
- Responsive design with dark mode toggle
- Static files served via WhiteNoise in production

## Tech Stack
- Django 5.x (Python 3)
- SQLite (default)
- Tailwind-css
- WhiteNoise for static files in production

## Quick Start

1) Create and activate a virtual environment
```sh
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
```

2) Install dependencies
```sh
pip install -r requirements.txt
```

3) Run migrations
```sh
python manage.py migrate
```

4) (Optional) Create a superuser
```sh
python manage.py createsuperuser
```

5) Start the development server
```sh
python manage.py runserver
```

Visit http://127.0.0.1:8000/

## Environment
The app works out-of-the-box with SQLite. Optional env vars:
- DJANGO_SECRET_KEY (defaults to a development key)
- DJANGO_DEBUG (set to "False" in production)

Allowed hosts are configured in [blog/settings.py](blog/settings.py).

## Static & Media
- Static files: served from `/static/` during development, collected to `/assets/` for production
- Media files: served from `/media/` (see [blog/urls.py](blog/urls.py) for DEBUG routing)

Collect static for production:
```sh
python manage.py collectstatic --no-input
```
You can also use the helper script:
```sh
bash build.sh
```

## CRUD Endpoints
- List posts: `/posts/`
- Create post: `/posts/new_post/`
- View a post: `/posts/<slug>/`
- Edit post: `/posts/<slug>/update/`
- My posts + delete flow: `/posts/my_posts/`

Authentication:
- Register: `/users/register/`
- Login: `/users/login/`
- Logout (POST): `/users/logout/`

🌍 Live Demo
🔗 https://obouizi.pythonanywhere.com
