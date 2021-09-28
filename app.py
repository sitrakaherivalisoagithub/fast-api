import uvicorn
from fastapi import FastAPI, Path
import json
from typing import Optional
from pydantic import BaseModel
app = FastAPI()

students = {
    1 : {
        "nom" : "Sitraka",
        "prenom" : "Herivals",
        "age": 21

    },
    2 : {
        "nom" : "Rakoto",
        "prenom": "ben",
        "age": 56
    }
}
class Student(BaseModel):
    nom : str
    prenom: str
    age: int

class UpdateStudent(BaseModel):
    nom : Optional[str] = None
    prenom: Optional[str] = None
    age: Optional[int] = None

@app.get("/")
def index():
    return {"name":"Sitraka"}

@app.get("/get-student/{student_id}")
def get_student(student_id: int = Path(None, decription = "Require id of students", gt=0)):
    if student_id not in students.keys():
        return {"error": "id not found"}
    return students[student_id]

@app.get("/all")
def get_all():
    
    return json.dumps(students)
@app.get("/get-by-name")
def get_by_name(nom: Optional[str] = None):
    for id, student in students.items():
        if student["nom"] == nom:
            return get_student(id)
    return {"data": "not found"}

@app. post("/create-student/{student_id}")
def create_student(student_id: int, student: Student):
    if student_id in students:
        return {"Error": "Student exists"}
    students[student_id] = student
    return students[student_id]

@app.put("/update-student/{student_id}")
def update_student(student_id: int, student: UpdateStudent):
    if student_id not in students:
        return {"error": "data not found"}
    
    if student.nom != None:
        students[student_id]["nom"] = student.nom
    if student.prenom != None:
        students[student_id]["prenom"] = student.prenom
    if student.age != None:
        students[student_id]["age"] = student.age
    return students[student_id]

@app.delete("/delete/{student_id}")
def delete(student_id: int):
    if student_id not in students:
        return {"error": "student not found"}
    return students.pop(student_id)


#if __name__ == "__main__":
#uvicorn app:app --reload

