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
