# Student Management System

## Project Overview

The **Student Management System** is a web-based application developed using Python and FastAPI. It helps users manage student information through a simple and user-friendly interface.

Users can add new students, view student details, and update existing student information.

This project was developed to practice Python Full Stack Development and understand how backend and frontend technologies work together.

## Technologies Used

- **Python** – Backend programming
- **FastAPI** – Backend web framework
- **HTML5** – Web page structure
- **CSS3** – Styling and user interface
- **Jinja2** – HTML templating

## Features

- Add new student details.
- View student information.
- Update existing student details.
- Display student profiles.
- User-friendly interface.
- Dynamic web pages using FastAPI and Jinja2.

## Student Information

The application manages student details such as:

- Student Name
- Age
- Gender
- Marks
- Course
- Student Image

## Project Structure

```text
Student-Management-System/
│
├── main.py
│
├── templates/
│   ├── index.html
│   ├── add_student.html
│   ├── update_student.html
│   └── view_student.html
│
└── README.md
```

*Note: The structure above is illustrative. Adjust the filenames to match your actual project.*

## Installation and Setup

### Step 1: Clone the Repository

```bash
git clone https://github.com/SKY-2003/Student-Management-System.git
```

### Step 2: Open the Project Folder

```bash
cd Student-Management-System
```

### Step 3: Install Required Packages

```bash
pip install fastapi uvicorn jinja2
```

### Step 4: Run the Application

```bash
python -m uvicorn main:app --reload
```

### Step 5: Open in Browser

Visit:

http://127.0.0.1:8000

## Learning Outcomes

Through this project, I gained practical experience in:

- Developing web applications using FastAPI.
- Understanding backend development with Python.
- Connecting HTML templates with backend routes.
- Working with Jinja2 templates.
- Handling student information.
- Implementing CRUD-related operations.
- Understanding the integration of frontend and backend technologies.

## Future Improvements

- Add student search functionality.
- Add student deletion functionality.
- Integrate a database for permanent data storage.
- Add user authentication and login functionality.

## Author

**Sandeep kumar Banda**

GitHub: https://github.com/SKY-2003

---

⭐ If you find this project useful, consider giving it a star!
