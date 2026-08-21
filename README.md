# 📚 Library Management System

A full-stack web-based **Library Management System** built with **Python, Flask, SQLite, HTML5, and CSS3** for managing college library operations digitally.

The application provides a centralized platform for administrators to manage books, students, book issue and return transactions, due dates, overdue books, and transaction history through a clean and responsive dashboard.

---

## 🚀 Project Overview

Traditional library management often involves manual records and repetitive data entry.

This project provides a simple digital solution that allows administrators to:

- Manage library books
- Manage student records
- Issue books
- Return books
- Track due dates
- Detect overdue books
- Maintain transaction history
- Monitor library statistics from a dashboard

The project was developed as a **college-level mini project** to demonstrate practical knowledge of Python backend development, database management, CRUD operations, authentication, and web development.

---

## ✨ Features

### 🔐 Admin Authentication

- Admin login
- Session-based authentication
- Protected dashboard and management pages
- Logout functionality
- Invalid login handling

### 📚 Book Management

- Add new books
- View all books
- Search books
- Edit book details
- Delete books
- Track total quantity
- Track available quantity
- Prevent issuing unavailable books

### 👨‍🎓 Student Management

- Register students
- View student records
- Search students
- Edit student information
- Delete student records
- Store name, email, phone, and course

### 📤 Book Issue Management

- Issue books to registered students
- Select available books
- Set due dates
- Automatically record issue date
- Update available book quantity
- Prevent unavailable books from being issued

### 📥 Book Return Management

- Return issued books
- Automatically record return date
- Update transaction status
- Increase available book quantity
- Maintain complete transaction records

### ⚠️ Due Date & Overdue Tracking

- Track due dates
- Detect overdue books
- Display overdue status
- Show overdue book count
- Prevent invalid due dates

### 📜 Transaction History

- View complete issue and return history
- Student details
- Book details
- Issue date
- Due date
- Return date
- Transaction status

### 📊 Dashboard

The dashboard provides quick statistics for:

- 📚 Total Books
- 📗 Available Books
- 📕 Issued Books
- 👨‍🎓 Total Students
- ⚠️ Overdue Books

---

## 🛠️ Technology Stack

| Technology | Purpose |
| Python | Backend Programming |
| Flask | Web Application Framework |
| SQLite | Relational Database |
| HTML5 | Frontend Structure |
| CSS3 | Styling & Responsive UI |
| Jinja2 | Dynamic Templates |
| Git | Version Control |
| GitHub | Source Code Management |

---

## 🏗️ System Architecture

```text
                    ┌─────────────────────┐
                    │      Admin User     │
                    └──────────┬──────────┘
                               │
                               ▼
                    ┌─────────────────────┐
                    │    Flask Web App    │
                    └──────────┬──────────┘
                               │
              ┌────────────────┼────────────────┐
              │                │                │
              ▼                ▼                ▼
        ┌──────────┐    ┌────────────┐   ┌─────────────┐
        │   Books  │    │  Students  │   │ Transactions│
        └──────────┘    └────────────┘   └──────┬──────┘
                                                 │
                                                 ▼
                                      ┌──────────────────┐
                                      │  SQLite Database │
                                      └──────────────────┘
```

🗄️ Database Design

The application uses SQLite with the following main tables.

Users

Stores administrator authentication information.

id
username
password
Students

Stores registered student information.

id
name
email
phone
course
Books

Stores library book information.

id
title
author
category
quantity
available_quantity
Issue Records

Stores book issue and return transactions.

id
student_id
book_id
issue_date
due_date
return_date
status
Database Relationship
Students ────────────┐
                     │
                     ▼
                Issue Records
                     ▲
                     │
Books ───────────────┘
📁 Project Structure
Library-Management-System/
│
├── app.py
├── .gitignore
├── README.md
│
├── static/
│   └── style.css
│
├── screenshots/
│   ├── 01-login.png
│   ├── 02-dashboard.png
│   ├── 03-books.png
│   ├── 04-students.png
│   ├── 05-issue-book.png
│   ├── 06-issued-books.png
│   └── 07-history.png
│
└── templates/
    ├── base.html
    ├── login.html
    ├── dashboard.html
    ├── books.html
    ├── add_book.html
    ├── edit_book.html
    ├── students.html
    ├── add_student.html
    ├── edit_student.html
    ├── issue_book.html
    ├── issued_books.html
    └── history.html
⚙️ Installation & Setup
1. Clone the Repository
git clone https://github.com/Harshada1441/Library-Management-System.git
2. Navigate to the Project
cd Library-Management-System
3. Create Virtual Environment
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
🔐 Demo Credentials

For demonstration purposes:

Username: admin
Password: admin123

For production applications, passwords should be securely hashed and sensitive credentials should not be stored directly in source code.

🔄 Application Workflow
Admin Login
     │
     ▼
 Dashboard
     │
     ├──────────────► Manage Books
     │
     ├──────────────► Manage Students
     │
     ├──────────────► Issue Book
     │                    │
     │                    ▼
     │              Issued Books
     │                    │
     │                    ▼
     │                Return Book
     │                    │
     └────────────────────┘
                          │
                          ▼
                       History

                       
📸 Application Screenshots

The following screenshots demonstrate the main modules of the application.


🔐 Admin Login

Secure admin login page for accessing the Library Management System.


📊 Dashboard

The dashboard provides an overview of books, students, issued books, available books, and overdue books.

📚 Book Management

Manage library books by adding, searching, editing, and deleting records.

👨‍🎓 Student Management

Manage registered student records including student information and course details.

📤 Issue Book

Issue available books to registered students and assign due dates.

📥 Issued Books

View currently issued books and manage book returns.

📜 Issue & Return History

View complete issue and return transaction history.

🎯 Core Concepts Demonstrated

This project demonstrates practical implementation of:

Python Programming
Flask Web Development
CRUD Operations
SQLite Database Management
SQL Queries
Database Relationships
Authentication
Session Management
Jinja2 Templating
HTML Forms
Input Validation
Search Functionality
Issue & Return Transactions
Date Validation
Overdue Detection
Responsive Web Design
Git & GitHub
💡 Learning Outcomes

Through this project, I gained practical experience in:

Designing relational databases
Connecting Flask with SQLite
Building CRUD functionality
Managing user sessions
Creating reusable Jinja2 templates
Handling form submissions
Implementing library business logic
Managing book availability
Building responsive dashboards
Using Git for version control
Publishing projects on GitHub
🔮 Future Enhancements

Planned improvements include:

📧 Email notifications for overdue books
💰 Automatic fine calculation
📊 Advanced dashboard analytics
📄 PDF report generation
📑 CSV export
🔎 Advanced filtering and sorting
👨‍🎓 Student login portal
🔑 Password hashing
👤 Admin profile management
📱 Improved mobile experience
☁️ Cloud database integration
🌐 Cloud deployment
🔔 Automated due-date reminders
📌 Project Status

Completed ✅

This project was developed as a college-level mini project to demonstrate practical skills in:

Python • Flask • SQLite • Web Development • Database Management • Git • GitHub

👩‍💻 Author
@Harshada Patil
Computer Engineering Graduate | Aspiring Data Scientist | Python Developer

GitHub:
https://github.com/Harshada1441
