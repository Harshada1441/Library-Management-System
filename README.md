# 📚 Library Management System

A professional web-based **Library Management System** built using **Python Flask and SQLite** to simplify and manage day-to-day college library operations.

The system provides a centralized platform for administrators to manage books, students, book issuing and returns, due dates, overdue books, and complete transaction history.

---

## 🚀 Project Overview

The **Library Management System** is designed for college libraries to reduce manual record keeping and provide an easy-to-use digital platform for managing library resources.

The application includes secure admin authentication, book and student management, issue/return tracking, overdue detection, and a dashboard for monitoring important library statistics.

---

## ✨ Key Features

### 🔐 Admin Authentication

- Secure admin login
- Session-based authentication
- Protected dashboard and management pages
- Logout functionality
- Invalid login error handling

### 📚 Book Management

- Add new books
- View all books
- Search books
- Update book information
- Delete books
- Track total book quantity
- Track available book quantity
- Prevent issuing unavailable books

### 👨‍🎓 Student Management

- Register new students
- View student records
- Search students
- Update student information
- Delete student records
- Store student name, email, phone and course

### 📤 Book Issue Management

- Issue books to registered students
- Select student and available book
- Set book due date
- Automatically record issue date
- Reduce available book quantity
- Prevent duplicate active book issues
- Prevent issuing unavailable books

### 📥 Book Return Management

- Return issued books
- Automatically record return date
- Update transaction status
- Increase available book quantity
- Maintain complete issue/return records

### ⚠️ Due Date & Overdue Tracking

- Track book due dates
- Detect overdue books
- Display overdue status
- Dashboard overdue book count
- Prevent selecting past due dates

### 📜 Transaction History

- Complete issue and return history
- Student details
- Book details
- Issue date
- Due date
- Return date
- Transaction status

### 📊 Dashboard

The dashboard provides quick statistics including:

- 📚 Total Books
- 📗 Available Books
- 📕 Issued Books
- 👨‍🎓 Total Students
- ⚠️ Overdue Books

### 🎨 User Interface

- Clean and professional dashboard
- Sidebar navigation
- Responsive design
- User-friendly forms
- Organized tables
- Status indicators
- Mobile-friendly layout

---

## 🛠️ Tech Stack

| Technology | Purpose |
|------------|---------|
| Python | Backend programming |
| Flask | Web application framework |
| SQLite | Database |
| HTML5 | Frontend structure |
| CSS3 | Styling and responsive UI |
| Jinja2 | Dynamic HTML templates |
| Git | Version control |
| GitHub | Source code management |

---

## 🗄️ Database Design

The application uses **SQLite** as the database.

### Main Tables

#### Users

Stores administrator authentication information.

```text
id
username
password



Students
## Stores registered student information.
id
name
email
phone
course


Books
## Stores library book information.
id
title
author
category
quantity
available_quantity


Issue Records
## Stores book issue and return transactions.
id
student_id
book_id
issue_date
due_date
return_date
status


## Database Relationships
                 ┌──────────────┐
                 │    Users     │
                 └──────────────┘
                        │
                        │ Authentication
                        │
                 ┌──────────────┐
                 │    Admin     │
                 └──────────────┘




┌──────────────┐                 ┌──────────────┐
│   Students   │                 │    Books     │
└──────┬───────┘                 └──────┬───────┘
       │                                │
       │                                │
       └──────────┐        ┌────────────┘
                  ▼        ▼
             ┌──────────────────┐
             │  Issue Records   │
             └──────────────────┘


## 📁 Project Structure
Library-Management-System/
│
├── app.py
├── .gitignore
├── README.md
│
├── static/
│   └── style.css
│
└── templates/
    │
    ├── base.html
    ├── login.html
    ├── dashboard.html
    │
    ├── books.html
    ├── add_book.html
    ├── edit_book.html
    │
    ├── students.html
    ├── add_student.html
    ├── edit_student.html
    │
    ├── issue_book.html
    ├── issued_books.html
    └── history.html

## ⚙️ Installation & Setup
1. Clone the Repository
git clone https://github.com/Harshada1441/Library-Management-System.git
2. Navigate to the Project
cd Library-Management-System
3. Create a Virtual Environment
python -m venv venv
4. Activate Virtual Environment
Windows
venv\Scripts\activate
macOS / Linux
source venv/bin/activate
5. Install Flask
pip install flask
6. Run the Application
python app.py
7. Open in Browser
http://127.0.0.1:5000


## 🔐 Demo Credentials
For demonstration purposes:
Username: admin
Password: admin123
For a production application, passwords should be securely hashed and sensitive credentials should not be stored directly in source code.

## 🔄 Application Workflow
                 ┌───────────────┐
                 │  Admin Login  │
                 └───────┬───────┘
                         │
                         ▼
                 ┌───────────────┐
                 │   Dashboard   │
                 └───────┬───────┘
                         │
          ┌──────────────┼──────────────┐
          │              │              │
          ▼              ▼              ▼
     ┌─────────┐   ┌───────────┐  ┌────────────┐
     │  Books  │   │ Students  │  │ Issue Book │
     └────┬────┘   └───────────┘  └─────┬──────┘
          │                              │
          │                              ▼
          │                       ┌─────────────┐
          │                       │Issued Books │
          │                       └──────┬──────┘
          │                              │
          │                              ▼
          │                       ┌─────────────┐
          │                       │Return Book  │
          │                       └──────┬──────┘
          │                              │
          └──────────────┬───────────────┘
                         ▼
                 ┌───────────────┐
                 │    History    │
                 └───────────────┘



##🎯 Core Concepts Demonstrated

This project demonstrates practical implementation of:

Python programming
Flask web development
CRUD operations
SQLite database management
SQL queries
Database relationships
Authentication
Session management
Jinja2 templating
HTML forms
Input validation
Search functionality
Issue/return transactions
Date validation
Overdue detection
Responsive web design
Git and GitHub


## 💡 What I Learned

Through this project, I gained practical experience in building a complete web application from scratch, including:

Designing a relational database
Connecting Flask with SQLite
Implementing CRUD functionality
Managing user sessions
Creating reusable Jinja2 templates
Handling form submissions
Implementing business logic for book issuing and returning
Managing book availability
Building a responsive dashboard
Using Git for version control
Publishing a project on GitHub


##🔮 Future Enhancements

The project can be further enhanced with:

📧 Email notifications for overdue books
💰 Automatic fine calculation
📊 Advanced dashboard charts
📄 PDF report generation
📑 CSV export
🔎 Advanced filtering and sorting
👨‍🎓 Student login portal
🔑 Password hashing
👤 Admin profile management
📱 Improved mobile application support
☁️ Cloud database integration
🌐 Deployment on a cloud platform
🔔 Automated due-date reminders


## 📸 Screenshots

Example:

### 🔐 Admin Login


![Admin Login](screenshots/login.png)


### 📊 Dashboard


![Dashboard](screenshots/dashboard.png)


### 📚 Books Management


![Books Management](screenshots/books.png)


### 👨‍🎓 Student Management


![Student Management](screenshots/students.png)


### 📤 Issue Book


![Issue Book](screenshots/issue-book.png)


### 📜 Transaction History


![Transaction History](screenshots/history.png)


## 👩‍💻 Author
Harshada Patil

Computer Engineering Graduate | Aspiring Data Scientist | Python Developer

GitHub:
https://github.com/Harshada1441


## ⭐ Support
If you find this project useful or interesting, consider giving the repository a ⭐ on GitHub.


##📌 Project Status
Status: Completed ✅
This project was developed as a college-level mini project to demonstrate practical skills in Python, Flask, SQLite, Web Development, Database Management, and Git/GitHub.
