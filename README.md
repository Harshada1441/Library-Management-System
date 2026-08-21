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
