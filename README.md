# 🌐 SocialHub — Django Social Media Platform

A fully-featured social media web application built with Django, SQLite, and custom CSS (no external frameworks).

---

## 🚀 Quick Start

### 1. Clone / Download the project
cd SocialMediaProject

### 2. (Optional) Create a virtual environment
python -m venv venv

Activate:
- Linux/Mac: source venv/bin/activate
- Windows: venv\Scripts\activate

### 3. Install dependencies
pip install -r requirements.txt

### 4. Run database migrations
python manage.py migrate

### 5. Start the development server
python manage.py runserver

### 6. Open in browser
http://127.0.0.1:8000/

---

## 🔐 Demo Login (Recommended)

Use this account to explore the application instantly:

Username: demo  
Password: demo123  

Or create a new account using the Signup option.

---

## 🧭 How to Use

1. Open the homepage  
2. Click Login or Signup  
3. Create and view posts  
4. Like, comment, and follow users  
5. Visit user profiles  

---

## ⚙️ Admin Panel (Optional)

Create admin user:
python manage.py createsuperuser

Open:
http://127.0.0.1:8000/admin/

---

## 🎯 Features

- User Authentication (Signup, Login, Logout)
- User Profiles (bio, profile photo, followers/following)
- Create Posts (with optional images)
- Global Feed
- Like/Unlike system (AJAX)
- Comments
- Follow/Unfollow users
- Search users
- Admin panel

---

## 🗄️ Database Models

- User (Django built-in)
- Profile (One-to-one with user)
- Post (content, image, timestamp)
- Comment (linked to user & post)
- Like (user-post relation)
- Follow (follower-following relation)

---

## 📁 Project Structure

SocialMediaProject/
├── manage.py
├── db.sqlite3
├── requirements.txt
├── SocialMediaProject/
├── app/
├── templates/
├── static/
└── media/

---

## 🛠️ Tech Stack

- Backend: Django (Python)
- Database: SQLite
- Frontend: HTML, CSS, JavaScript
- Templates: Django Templates

---

## 📝 Notes

- Login & Signup available on homepage  
- Demo data may be included  
- Media files stored in `media/`  
- Uses Django authentication system  
- No external CSS frameworks  
- AJAX used for like feature  

---

## ✅ Project Status

✔ Fully functional  
✔ Clean UI  
✔ Ready for submission  
