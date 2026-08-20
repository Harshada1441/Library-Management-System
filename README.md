# 📚 Library Management System

A professional web-based **Library Management System** built using **Python Flask and SQLite** to manage college library operations.

The system allows administrators to manage books, students, book issuing, returns, due dates, overdue books, and transaction history.

---

## ✨ Key Features

### 🔐 Admin Authentication

- Secure admin login
- Session-based authentication
- Protected dashboard
- Logout functionality

### 📚 Book Management

- Add books
- View books
- Search books
- Update books
- Delete books
- Track total and available quantities

### 👨‍🎓 Student Management

- Register students
- View students
- Search students
- Update student information
- Delete students

### 📤 Book Issue

- Issue books to students
- Select available books
- Set due dates
- Record issue date
- Update book availability

### 📥 Book Return

- Return issued books
- Record return date
- Update transaction status
- Update book availability

### ⚠️ Overdue Tracking

- Track due dates
- Detect overdue books
- Display overdue status
- Show overdue count on dashboard

### 📜 Transaction History

- View issue history
- View return history
- Student details
- Book details
- Issue date
- Due date
- Return date
- Status

### 📊 Dashboard

- 📚 Total Books
- 📗 Available Books
- 📕 Issued Books
- 👨‍🎓 Total Students
- ⚠️ Overdue Books

---

## 🛠️ Tech Stack

| Technology | Purpose |
|---|---|
| Python | Backend |
| Flask | Web Framework |
| SQLite | Database |
| HTML5 | Frontend |
| CSS3 | Styling |
| Jinja2 | Templates |
| Git | Version Control |
| GitHub | Source Code Management |

---

## 🗄️ Database Design

The application uses **SQLite**.

### Users

Stores administrator login information.

```text
id
username
password