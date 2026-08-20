from flask import (
    Flask,
    render_template,
    request,
    redirect,
    url_for,
    session
)

from datetime import date
import sqlite3

from functools import wraps

from werkzeug.security import generate_password_hash, check_password_hash


app = Flask(__name__)

app.secret_key = "library_secret_key"

DATABASE = "library.db"


# =========================================================
# DATABASE CONNECTION
# =========================================================

def get_db_connection():

    conn = sqlite3.connect(DATABASE)

    conn.row_factory = sqlite3.Row

    # Enable foreign key support
    conn.execute("PRAGMA foreign_keys = ON")

    return conn


# =========================================================
# INITIALIZE DATABASE
# =========================================================

def init_db():

    conn = get_db_connection()

    # Users table
    conn.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE NOT NULL,
            password TEXT NOT NULL
        )
    """)

    # Students table
    conn.execute("""
        CREATE TABLE IF NOT EXISTS students (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            email TEXT UNIQUE NOT NULL,
            phone TEXT,
            course TEXT
        )
    """)

    # Books table
    conn.execute("""
        CREATE TABLE IF NOT EXISTS books (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            author TEXT NOT NULL,
            category TEXT,
            quantity INTEGER NOT NULL,
            available_quantity INTEGER NOT NULL
        )
    """)

    # Issue / Return table
    conn.execute("""
        CREATE TABLE IF NOT EXISTS issue_records (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            student_id INTEGER NOT NULL,
            book_id INTEGER NOT NULL,
            issue_date TEXT NOT NULL,
            due_date TEXT NOT NULL,
            return_date TEXT,
            status TEXT NOT NULL,
            FOREIGN KEY (student_id) REFERENCES students(id),
            FOREIGN KEY (book_id) REFERENCES books(id)
        )
    """)

    # -----------------------------------------------------
    # Default Admin
    # -----------------------------------------------------

    admin = conn.execute(
        """
        SELECT * FROM users
        WHERE username = ?
        """,
        ("admin",)
    ).fetchone()

    if admin is None:

        hashed_password = generate_password_hash("admin123")

        conn.execute(
            """
            INSERT INTO users
            (username, password)
            VALUES (?, ?)
            """,
            (
                "admin",
                hashed_password
            )
        )

    conn.commit()

    conn.close()


# =========================================================
# LOGIN REQUIRED DECORATOR
# =========================================================

def login_required(func):

    @wraps(func)
    def wrapper(*args, **kwargs):

        if "user_id" not in session:

            return redirect(url_for("login"))

        return func(*args, **kwargs)

    return wrapper


# =========================================================
# HOME
# =========================================================

@app.route("/")
def home():

    return redirect(url_for("login"))


# =========================================================
# LOGIN
# =========================================================

@app.route("/login", methods=["GET", "POST"])
def login():

    if "user_id" in session:

        return redirect(url_for("dashboard"))

    if request.method == "POST":

        username = request.form.get("username", "").strip()

        password = request.form.get("password", "")

        conn = get_db_connection()

        user = conn.execute(
            """
            SELECT * FROM users
            WHERE username = ?
            """,
            (username,)
        ).fetchone()

        # -------------------------------------------------
        # Password verification
        # -------------------------------------------------

        valid_password = False

        if user:

            stored_password = user["password"]

            # New hashed password
            try:

                valid_password = check_password_hash(
                    stored_password,
                    password
                )

            except ValueError:

                valid_password = False

            # -------------------------------------------------
            # Backward compatibility for old plain password
            # -------------------------------------------------

            if not valid_password and stored_password == password:

                valid_password = True

                # Convert old plain password to hash
                new_password = generate_password_hash(password)

                conn.execute(
                    """
                    UPDATE users
                    SET password = ?
                    WHERE id = ?
                    """,
                    (
                        new_password,
                        user["id"]
                    )
                )

                conn.commit()

        conn.close()

        if user and valid_password:

            session["user_id"] = user["id"]

            session["username"] = user["username"]

            return redirect(url_for("dashboard"))

        return render_template(
            "login.html",
            error="Invalid username or password"
        )

    return render_template("login.html")


# =========================================================
# DASHBOARD
# =========================================================

@app.route("/dashboard")
@login_required
def dashboard():

    conn = get_db_connection()

    # Total books
    total_books = conn.execute(
        """
        SELECT COUNT(*) AS count
        FROM books
        """
    ).fetchone()["count"]

    # Total students
    total_students = conn.execute(
        """
        SELECT COUNT(*) AS count
        FROM students
        """
    ).fetchone()["count"]

    # Currently issued books
    issued_books = conn.execute(
        """
        SELECT COUNT(*) AS count
        FROM issue_records
        WHERE status = 'Issued'
        """
    ).fetchone()["count"]

    # Available books
    available_books = conn.execute(
        """
        SELECT COALESCE(
            SUM(available_quantity),
            0
        ) AS count
        FROM books
        """
    ).fetchone()["count"]

    # Overdue books
    overdue_books = conn.execute(
        """
        SELECT COUNT(*) AS count
        FROM issue_records
        WHERE status = 'Issued'
        AND due_date < date('now')
        """
    ).fetchone()["count"]

    conn.close()

    return render_template(
        "dashboard.html",
        username=session.get("username"),
        total_books=total_books,
        total_students=total_students,
        issued_books=issued_books,
        available_books=available_books,
        overdue_books=overdue_books
    )


# =========================================================
# BOOKS
# =========================================================

@app.route("/books")
@login_required
def books():

    search = request.args.get(
        "search",
        ""
    ).strip()

    conn = get_db_connection()

    if search:

        books = conn.execute(
            """
            SELECT * FROM books

            WHERE title LIKE ?
            OR author LIKE ?
            OR category LIKE ?

            ORDER BY id DESC
            """,
            (
                f"%{search}%",
                f"%{search}%",
                f"%{search}%"
            )
        ).fetchall()

    else:

        books = conn.execute(
            """
            SELECT * FROM books
            ORDER BY id DESC
            """
        ).fetchall()

    conn.close()

    return render_template(
        "books.html",
        books=books,
        search=search
    )


# =========================================================
# ADD BOOK
# =========================================================

@app.route("/books/add", methods=["GET", "POST"])
@login_required
def add_book():

    if request.method == "POST":

        title = request.form.get(
            "title",
            ""
        ).strip()

        author = request.form.get(
            "author",
            ""
        ).strip()

        category = request.form.get(
            "category",
            ""
        ).strip()

        try:

            quantity = int(
                request.form.get(
                    "quantity",
                    0
                )
            )

        except ValueError:

            return "Quantity must be a valid number."

        if not title or not author:

            return "Title and author are required."

        if quantity <= 0:

            return "Quantity must be greater than zero."

        conn = get_db_connection()

        conn.execute(
            """
            INSERT INTO books
            (
                title,
                author,
                category,
                quantity,
                available_quantity
            )

            VALUES (?, ?, ?, ?, ?)
            """,
            (
                title,
                author,
                category,
                quantity,
                quantity
            )
        )

        conn.commit()

        conn.close()

        return redirect(url_for("books"))

    return render_template("add_book.html")


# =========================================================
# EDIT BOOK
# =========================================================

@app.route(
    "/books/edit/<int:book_id>",
    methods=["GET", "POST"]
)
@login_required
def edit_book(book_id):

    conn = get_db_connection()

    book = conn.execute(
        """
        SELECT * FROM books
        WHERE id = ?
        """,
        (book_id,)
    ).fetchone()

    if book is None:

        conn.close()

        return "Book not found", 404

    if request.method == "POST":

        title = request.form.get(
            "title",
            ""
        ).strip()

        author = request.form.get(
            "author",
            ""
        ).strip()

        category = request.form.get(
            "category",
            ""
        ).strip()

        try:

            quantity = int(
                request.form.get(
                    "quantity",
                    0
                )
            )

        except ValueError:

            conn.close()

            return "Quantity must be a valid number."

        if quantity <= 0:

            conn.close()

            return "Quantity must be greater than zero."

        if not title or not author:

            conn.close()

            return "Title and author are required."

        # Books currently issued
        issued_count = (
            book["quantity"]
            - book["available_quantity"]
        )

        if quantity < issued_count:

            conn.close()

            return (
                "Quantity cannot be less than "
                "currently issued books."
            )

        available_quantity = (
            quantity - issued_count
        )

        conn.execute(
            """
            UPDATE books

            SET title = ?,
                author = ?,
                category = ?,
                quantity = ?,
                available_quantity = ?

            WHERE id = ?
            """,
            (
                title,
                author,
                category,
                quantity,
                available_quantity,
                book_id
            )
        )

        conn.commit()

        conn.close()

        return redirect(url_for("books"))

    conn.close()

    return render_template(
        "edit_book.html",
        book=book
    )


# =========================================================
# DELETE BOOK
# =========================================================

@app.route("/books/delete/<int:book_id>")
@login_required
def delete_book(book_id):

    conn = get_db_connection()

    book = conn.execute(
        """
        SELECT * FROM books
        WHERE id = ?
        """,
        (book_id,)
    ).fetchone()

    if book is None:

        conn.close()

        return "Book not found", 404

    # Don't delete books with history
    issue_record = conn.execute(
        """
        SELECT id FROM issue_records
        WHERE book_id = ?
        LIMIT 1
        """,
        (book_id,)
    ).fetchone()

    if issue_record:

        conn.close()

        return (
            "This book cannot be deleted "
            "because it has issue/return history."
        )

    conn.execute(
        """
        DELETE FROM books
        WHERE id = ?
        """,
        (book_id,)
    )

    conn.commit()

    conn.close()

    return redirect(url_for("books"))


# =========================================================
# ISSUE BOOK
# =========================================================
# =========================================================
# ISSUE BOOK
# =========================================================

@app.route(
    "/issue-book",
    methods=["GET", "POST"]
)
@login_required
def issue_book():

    conn = get_db_connection()

    if request.method == "POST":

        student_id = request.form.get(
            "student_id"
        )

        book_id = request.form.get(
            "book_id"
        )

        due_date = request.form.get(
            "due_date"
        )

        today = date.today().isoformat()

        # -------------------------------------------------
        # Validate due date
        # -------------------------------------------------

        if not due_date:

            conn.close()

            return "Due date is required."

        if due_date < today:

            conn.close()

            return "Due date cannot be in the past."

        # -------------------------------------------------
        # Check student
        # -------------------------------------------------

        student = conn.execute(
            """
            SELECT * FROM students
            WHERE id = ?
            """,
            (student_id,)
        ).fetchone()

        if student is None:

            conn.close()

            return "Student not found."

        # -------------------------------------------------
        # Check book
        # -------------------------------------------------

        book = conn.execute(
            """
            SELECT * FROM books
            WHERE id = ?
            """,
            (book_id,)
        ).fetchone()

        if book is None:

            conn.close()

            return "Book not found."

        # -------------------------------------------------
        # Check availability
        # -------------------------------------------------

        if book["available_quantity"] <= 0:

            conn.close()

            return "This book is currently unavailable."

        # -------------------------------------------------
        # Prevent duplicate active issue
        # -------------------------------------------------

        existing_issue = conn.execute(
            """
            SELECT id
            FROM issue_records

            WHERE student_id = ?
            AND book_id = ?
            AND status = 'Issued'
            """,
            (
                student_id,
                book_id
            )
        ).fetchone()

        if existing_issue:

            conn.close()

            return (
                "This student already has "
                "this book issued."
            )

        # -------------------------------------------------
        # Issue book
        # -------------------------------------------------

        issue_date = today

        conn.execute(
            """
            INSERT INTO issue_records
            (
                student_id,
                book_id,
                issue_date,
                due_date,
                status
            )

            VALUES (?, ?, ?, ?, ?)
            """,
            (
                student_id,
                book_id,
                issue_date,
                due_date,
                "Issued"
            )
        )

        # Reduce available quantity

        conn.execute(
            """
            UPDATE books

            SET available_quantity =
                available_quantity - 1

            WHERE id = ?
            """,
            (book_id,)
        )

        conn.commit()

        conn.close()

        return redirect(
            url_for("issued_books")
        )

    # -----------------------------------------------------
    # Get Students
    # -----------------------------------------------------

    students = conn.execute(
        """
        SELECT *
        FROM students
        ORDER BY name
        """
    ).fetchall()

    # -----------------------------------------------------
    # Get Available Books
    # -----------------------------------------------------

    books = conn.execute(
        """
        SELECT *
        FROM books
        WHERE available_quantity > 0
        ORDER BY title
        """
    ).fetchall()

    conn.close()

    # -----------------------------------------------------
    # Send today's date to HTML
    # -----------------------------------------------------

    return render_template(
        "issue_book.html",
        students=students,
        books=books,
        today=date.today().isoformat()
    )

# =========================================================
# ISSUED BOOKS
# =========================================================

# =========================================================
# ISSUED BOOKS
# =========================================================

@app.route("/issued-books")
@login_required
def issued_books():

    conn = get_db_connection()

    records = conn.execute(
        """
        SELECT
            issue_records.id,
            students.name AS student_name,
            books.title AS book_title,
            issue_records.issue_date,
            issue_records.due_date,
            issue_records.return_date,
            issue_records.status

        FROM issue_records

        JOIN students
        ON issue_records.student_id = students.id

        JOIN books
        ON issue_records.book_id = books.id

        ORDER BY issue_records.id DESC
        """
    ).fetchall()

    conn.close()

    return render_template(
        "issued_books.html",
        records=records,
        today=date.today().isoformat()
    )


# =========================================================
# RETURN BOOK
# =========================================================

@app.route("/return-book/<int:record_id>")
@login_required
def return_book(record_id):

    conn = get_db_connection()

    # Get issue record
    record = conn.execute(
        """
        SELECT *
        FROM issue_records
        WHERE id = ?
        """,
        (record_id,)
    ).fetchone()

    if record is None:

        conn.close()

        return "Issue record not found.", 404

    # Already returned
    if record["status"] == "Returned":

        conn.close()

        return "This book has already been returned."

    # Return date
    return_date = date.today().isoformat()

    # Update issue record
    conn.execute(
        """
        UPDATE issue_records

        SET return_date = ?,
            status = 'Returned'

        WHERE id = ?
        """,
        (
            return_date,
            record_id
        )
    )

    # Increase availability
    conn.execute(
        """
        UPDATE books

        SET available_quantity =
            available_quantity + 1

        WHERE id = ?
        """,
        (record["book_id"],)
    )

    conn.commit()

    conn.close()

    return redirect(
        url_for("issued_books")
    )


# =========================================================
# STUDENTS
# =========================================================

@app.route("/students")
@login_required
def students():

    search = request.args.get(
        "search",
        ""
    ).strip()

    conn = get_db_connection()

    if search:

        students = conn.execute(
            """
            SELECT *
            FROM students

            WHERE name LIKE ?
            OR email LIKE ?
            OR course LIKE ?

            ORDER BY id DESC
            """,
            (
                f"%{search}%",
                f"%{search}%",
                f"%{search}%"
            )
        ).fetchall()

    else:

        students = conn.execute(
            """
            SELECT *
            FROM students
            ORDER BY id DESC
            """
        ).fetchall()

    conn.close()

    return render_template(
        "students.html",
        students=students,
        search=search
    )


# =========================================================
# ADD STUDENT
# =========================================================

@app.route(
    "/students/add",
    methods=["GET", "POST"]
)
@login_required
def add_student():

    if request.method == "POST":

        name = request.form.get(
            "name",
            ""
        ).strip()

        email = request.form.get(
            "email",
            ""
        ).strip()

        phone = request.form.get(
            "phone",
            ""
        ).strip()

        course = request.form.get(
            "course",
            ""
        ).strip()

        if not name or not email or not course:

            return (
                "Name, email and course "
                "are required."
            )

        conn = get_db_connection()

        try:

            conn.execute(
                """
                INSERT INTO students
                (
                    name,
                    email,
                    phone,
                    course
                )

                VALUES (?, ?, ?, ?)
                """,
                (
                    name,
                    email,
                    phone,
                    course
                )
            )

            conn.commit()

        except sqlite3.IntegrityError:

            conn.close()

            return (
                "A student with this email "
                "already exists."
            )

        conn.close()

        return redirect(
            url_for("students")
        )

    return render_template(
        "add_student.html"
    )


# =========================================================
# EDIT STUDENT
# =========================================================

@app.route(
    "/students/edit/<int:student_id>",
    methods=["GET", "POST"]
)
@login_required
def edit_student(student_id):

    conn = get_db_connection()

    student = conn.execute(
        """
        SELECT *
        FROM students
        WHERE id = ?
        """,
        (student_id,)
    ).fetchone()

    if student is None:

        conn.close()

        return "Student not found.", 404

    if request.method == "POST":

        name = request.form.get(
            "name",
            ""
        ).strip()

        email = request.form.get(
            "email",
            ""
        ).strip()

        phone = request.form.get(
            "phone",
            ""
        ).strip()

        course = request.form.get(
            "course",
            ""
        ).strip()

        if not name or not email or not course:

            conn.close()

            return (
                "Name, email and course "
                "are required."
            )

        try:

            conn.execute(
                """
                UPDATE students

                SET name = ?,
                    email = ?,
                    phone = ?,
                    course = ?

                WHERE id = ?
                """,
                (
                    name,
                    email,
                    phone,
                    course,
                    student_id
                )
            )

            conn.commit()

        except sqlite3.IntegrityError:

            conn.close()

            return (
                "A student with this email "
                "already exists."
            )

        conn.close()

        return redirect(
            url_for("students")
        )

    conn.close()

    return render_template(
        "edit_student.html",
        student=student
    )


# =========================================================
# DELETE STUDENT
# =========================================================

@app.route(
    "/students/delete/<int:student_id>"
)
@login_required
def delete_student(student_id):

    conn = get_db_connection()

    student = conn.execute(
        """
        SELECT *
        FROM students
        WHERE id = ?
        """,
        (student_id,)
    ).fetchone()

    if student is None:

        conn.close()

        return "Student not found.", 404

    # Don't delete students with history
    issue_record = conn.execute(
        """
        SELECT id
        FROM issue_records
        WHERE student_id = ?
        LIMIT 1
        """,
        (student_id,)
    ).fetchone()

    if issue_record:

        conn.close()

        return (
            "This student cannot be deleted "
            "because they have issue/return history."
        )

    conn.execute(
        """
        DELETE FROM students
        WHERE id = ?
        """,
        (student_id,)
    )

    conn.commit()

    conn.close()

    return redirect(
        url_for("students")
    )


# =========================================================
# HISTORY
# =========================================================

@app.route("/history")
@login_required
def history():

    today = date.today().isoformat()

    conn = get_db_connection()

    rows = conn.execute(
        """
        SELECT

            issue_records.id,

            students.name AS student_name,

            books.title AS book_title,

            issue_records.issue_date,

            issue_records.due_date,

            issue_records.return_date,

            issue_records.status

        FROM issue_records

        JOIN students
        ON issue_records.student_id = students.id

        JOIN books
        ON issue_records.book_id = books.id

        ORDER BY issue_records.id DESC
        """
    ).fetchall()

    records = []

    for row in rows:

        record = dict(row)

        record["overdue"] = (
            record["status"] == "Issued"
            and record["due_date"] < today
        )

        records.append(record)

    conn.close()

    return render_template(
        "history.html",
        records=records
    )


# =========================================================
# LOGOUT
# =========================================================

@app.route("/logout")
def logout():

    session.clear()

    return redirect(
        url_for("login")
    )


# =========================================================
# RUN APPLICATION
# =========================================================

if __name__ == "__main__":

    init_db()

    app.run(
        debug=True
    )