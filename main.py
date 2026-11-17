from fastapi import FastAPI,Request,Form
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel,Field
from fastapi.responses import RedirectResponse

import sqlite3
class Student(BaseModel):
    name : str 
    age: int = Field(ge=18, le=30)
    gender: str
    marks: int
    course: str
    image:str
    status: int


def get_connection():
    connection = sqlite3.connect(
        "students.db"
    )
    return connection


get_connection()


def create_table():
    connection = get_connection()
    cursor = connection.cursor()

    q = """
    CREATE TABLE IF NOT EXISTS students(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    age INTEGER,
    gender TEXT,
    marks INTEGER,
    course TEXT,
    image TEXT,
    status INTEGER
    )
    """
    cursor.execute(q)
    connection.commit()
    connection.close()

create_table()



templates = Jinja2Templates(
    directory="templates"
)


app = FastAPI()


@app.get("/")
def home(req:Request):
    connection = get_connection()
    cursor = connection.cursor()

    q = "select * from students"


    cursor.execute(q)
    students = cursor.fetchall()
    print(students)
    connection.close()

    return templates.TemplateResponse(
            request=req,
            name="home.html",
            context={"stds":students}
        )


@app.get("/students/add")
def send_std_form(req:Request):
    return templates.TemplateResponse(
        request=req,
        name="add-student.html",
        context={}
    )


@app.post("/students/add")
def create_std(
    name = Form(),
    age = Form(),
    gender = Form(),
    marks = Form(),
    course = Form(),
    image = Form(),
    status = Form()
    ):
    student = Student(
        name = name,
        age = age,
        gender = gender,
        marks = marks,
        course = course,
        image = image,
        status = status
    )
    values = (student.name, student.age, student.gender, student.marks, student.course, student.image, student.status)

    connection = get_connection()
    cursor = connection.cursor()

    q = """
    INSERT INTO students
    (name, age, gender, marks, course, image, status)
    VALUES (?, ?, ?, ?, ?, ?, ?)
    """
    cursor.execute(q, values)
    connection.commit()
    connection.close()
    
    return RedirectResponse("/", status_code=303)

@app.get("/students/update/{student_id}")
def show_update_form(student_id: int, req: Request):

    connection = get_connection()
    cursor = connection.cursor()

    q = "SELECT * FROM students WHERE id = ?"
    cursor.execute(q, (student_id,))

    student = cursor.fetchone()

    connection.close()

    if student is None:
        return {"message": "Student not found"}

    return templates.TemplateResponse(
        request=req,
        name="update-student.html",
        context={"student": student}
    )


@app.post("/students/update/{student_id}")
def update_student(
    student_id: int,
    name: str = Form(),
    age: int = Form(),
    gender: str = Form(),
    marks: int = Form(),
    course: str = Form(),
    image: str = Form(),
    status: int = Form()
):

    student = Student(
        name=name,
        age=age,
        gender=gender,
        marks=marks,
        course=course,
        image=image,
        status=status
    )

    connection = get_connection()
    cursor = connection.cursor()

    q = """
    UPDATE students
    SET name=?,
        age=?,
        gender=?,
        marks=?,
        course=?,
        image=?, 
        status=?
         WHERE id=?
    """

    values = (
        student.name, student.age, student.gender,
        student.marks, student.course, student.image,
        student.status, student_id
    )

    cursor.execute(q, values)
    connection.commit()
    connection.close()

    return RedirectResponse("/", status_code=303)

@app.get("/students/view/{student_id}")
def view_student(student_id: int, req: Request):

    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute(
        "SELECT * FROM students WHERE id=?",
        (student_id,)
    )

    std = cursor.fetchone()

    connection.close()

    if std is None:
        return {"message": "Student not found"}

    return templates.TemplateResponse(
        request=req,
        name="view-student.html",
        context={"std": std}
    )
@app.post("/students/delete/{student_id}")
def delete_student(student_id: int):

    connection = get_connection()
    cursor = connection.cursor()

    q = "DELETE FROM students WHERE id=?"

    cursor.execute(q, (student_id,))

    connection.commit()
    connection.close()

    return RedirectResponse("/", status_code=303)




