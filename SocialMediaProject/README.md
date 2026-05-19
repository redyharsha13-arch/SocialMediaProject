# 🌐 SocialHub — Django Social Media Platform

A fully-featured social media web application built with Django, SQLite, and Bootstrap-free custom CSS.

---

## 🚀 Quick Start

### 1. Clone / Download the project
```bash
cd SocialMediaProject
```

### 2. (Optional) Create a virtual environment
```bash
python -m venv venv
source venv/bin/activate       # Linux/Mac
venv\Scripts\activate          # Windows
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Run database migrations
```bash
python manage.py migrate
```

### 5. (Optional) Create a superuser for admin panel
```bash
python manage.py createsuperuser
```

### 6. Start the development server
```bash
python manage.py runserver
```

### 7. Open in browser
```
http://127.0.0.1:8000/
```

**Admin Panel:** `http://127.0.0.1:8000/admin/`

---

## 🎯 Features

| Feature | Description |
|---|---|
| **User Auth** | Signup, Login, Logout |
| **Profiles** | Bio, profile photo, followers/following counts |
| **Posts** | Create text posts with optional image upload |
| **Feed** | Global home feed with all posts |
| **Likes** | Like/unlike posts (AJAX, no page reload) |
| **Comments** | Add comments under posts |
| **Follow** | Follow/unfollow other users |
| **Search** | Search users by username |
| **Admin** | Full Django admin panel at /admin/ |

---

## 🗄️ Database Models

- **User** — Django's built-in auth user
- **Profile** — bio, profile image (OneToOne with User)
- **Post** — content, optional image, timestamp
- **Comment** — text, linked to user + post
- **Like** — unique user + post pair
- **Follow** — follower + following user pair

---

## 📁 Project Structure

```
SocialMediaProject/
├── manage.py
├── db.sqlite3              ← Created after migrations
├── requirements.txt
├── SocialMediaProject/     ← Django project config
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── app/                    ← Main application
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   ├── forms.py
│   └── admin.py
├── templates/              ← HTML templates
│   ├── base.html
│   ├── home.html
│   ├── login.html
│   ├── signup.html
│   ├── profile.html
│   ├── edit_profile.html
│   ├── create_post.html
│   └── search.html
├── static/
│   ├── css/style.css
│   └── js/main.js
└── media/                  ← Uploaded images (auto-created)
```

---

## 🛠️ Tech Stack

- **Backend:** Python 3.x + Django 4.x
- **Database:** SQLite (db.sqlite3)
- **Frontend:** HTML5, CSS3, Vanilla JavaScript
- **Templating:** Django Templates (server-side rendering)
- **Images:** Pillow (for image uploads)

---

## 📝 Notes

- All uploaded media (profile/post images) are saved to the `media/` folder
- The project uses Django's built-in authentication system
- No external CSS frameworks — all styles are custom
- AJAX is used for like toggle (no page reload)
