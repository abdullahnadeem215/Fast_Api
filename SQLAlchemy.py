from sqlalchemy import create_engine,Column,String,Integer
from sqlalchemy.orm import sessionmaker,Session,declarative_base
from fastapi import FastAPI,Depends

app = FastAPI()

DATA_BASE = "sqlite:///./DATABASE.db"

engine  = create_engine(
    DATA_BASE,
    connect_args={"check_same_thread":False}
)

local_session= sessionmaker(bind=engine)
Base = declarative_base()

class Student(Base):
    __tablename__="Student"

    student_id = Column(Integer,primary_key=True,index=True)
    student_name = Column(String)
    student_roll_no = Column(String,unique=True)

Base.metadata.create_all(bind=engine)

def get_db():
    db = local_session()
    try:
        yield db
    finally:
        db.close()



@app.post("/CreateStudent")
def create_student(name:str,roll_no:str,db:Session=Depends(get_db)):
    student = Student(student_name=name,student_roll_no=roll_no)
    db.add(student)
    db.commit()
    db.refresh(student)
    return {
        "status":"Added Successfully...",
        "Data":student
    }
@app.get("/all_students")
def getStudents(db:Session=Depends(get_db)):
    student = db.query(Student).all()
    return {
        "Total Students":len(student),
        "Students":student
    }