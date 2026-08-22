# Harmoon

A Django-based appointment reservation web application designed to provide a simple and user-friendly booking experience.

Harmoon allows users to browse available reservation dates, select appointment time slots, manage their account, and view their reservations.

## ✨ Features

* Appointment reservation interface
* Display of available dates for the next 20 days
* Half-hour appointment time slots
* User account section
* User registration form
* Reservation history for authenticated users
* Responsive Persian RTL interface
* Django Admin panel
* Modular Django application structure
* SQLite database
* Custom CSS styling
* Tailwind CSS integration
* Font Awesome icons

## 🛠 Tech Stack

**Backend**

* Python
* Django 4.2
* SQLite

**Frontend**

* HTML5
* CSS3
* Django Templates
* Tailwind CSS
* Font Awesome

## 📂 Project Structure

```text
harmoon_project/
│
├── account_module/
│   ├── migrations/
│   ├── static/
│   ├── templates/
│   ├── forms.py
│   ├── models.py
│   ├── urls.py
│   └── views.py
│
├── home_module/
│   ├── migrations/
│   ├── static/
│   ├── templates/
│   ├── models.py
│   ├── urls.py
│   └── views.py
│
├── reservation_module/
│   ├── migrations/
│   ├── static/
│   ├── templates/
│   ├── models.py
│   ├── urls.py
│   └── views.py
│
├── harmoon_project/
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
│
├── static/
├── templates/
├── db.sqlite3
├── manage.py
└── .gitignore
```

## 🚀 Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/Brbodd/harmoon_project.git
cd harmoon_project
```

### 2. Create a virtual environment

```bash
python -m venv venv
```

Activate the virtual environment.

**Windows**

```bash
venv\Scripts\activate
```

**macOS / Linux**

```bash
source venv/bin/activate
```

### 3. Install Django

```bash
pip install django==4.2
```

### 4. Apply migrations

```bash
python manage.py migrate
```

### 5. Run the development server

```bash
python manage.py runserver
```

Open the application in your browser:

```text
http://127.0.0.1:8000/
```

## 📅 Reservation System

The reservation section dynamically generates the next **20 available days** from the current date.

Users can select a date and then choose from appointment time slots ranging from:

```text
10:00
10:30
11:00
...
18:00
18:30
```

The reservation data model stores:

```text
User
Date
Time
```

Each reservation is associated with a Django user account.

## 👤 Account System

The project includes an account module for managing users.

The account page can display reservations associated with the currently logged-in user.

The registration interface currently includes fields such as:

* Full name
* Phone number

Further authentication and registration functionality can be extended as the project develops.

## 🗄 Database Models

### Profile

Stores additional information for each user:

```text
User
Phone Number
```

### Reservation

Stores appointment information:

```text
User
Date
Time
```

## 🗺 URL Structure

```text
/                       Home page
/reservation/            Reservation section
/account/                Account section
/admin/                  Django Admin
```

## 🔮 Future Improvements

Possible improvements for future versions include:

* Complete user authentication and registration
* Login and logout system
* Saving selected reservation slots
* Preventing duplicate reservations
* Displaying unavailable time slots
* Reservation cancellation
* User profile management
* Email or SMS appointment confirmation
* Admin reservation management
* REST API implementation
* PostgreSQL support
* Deployment configuration
* Automated tests

## 👨‍💻 Author

**Barbod Zahedi**

GitHub: [@Brbodd](https://github.com/Brbodd)

## 📄 License

This project is intended for educational and development purposes.
