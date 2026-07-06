from sqlalchemy import create_engine,Column,String,Integer
from sqlalchemy.orm import sessionmaker,Session,declarative_base
from fastapi import FastAPI,Depends,HTTPException

app = FastAPI()


###Create the URl for telling the location where our database would be located
DATA_BASE = "sqlite:///./DATABASE.db"

####Create an engine to initialize the database with sqlalchemy
engine  = create_engine(
    DATA_BASE,
    connect_args={"check_same_thread":False}
)

###create a Session for the database
local_session= sessionmaker(bind=engine)

###Create the base to ientify this is links to the database
Base = declarative_base()

###Design Schema for the database
class Student(Base):
    __tablename__="Student"

    student_id = Column(Integer,primary_key=True,index=True)
    student_name = Column(String)
    student_roll_no = Column(String,unique=True)


####Execute the querys from the base class
Base.metadata.create_all(bind=engine)


### Function to get the db Session
def get_db():
    db = local_session()
    try:
        yield db
    finally:
        db.close()


###Crate data in database
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


###Read Database
@app.get("/all_students")
def getStudents(db:Session=Depends(get_db)):
    student = db.query(Student).all()
    return {
        "Total Students":len(student),
        "Students":student
    }
###get Student by id
@app.get("/student/{student_id}")
def get_student_by_ID(id:int,db:Session=Depends(get_db)):
    student = db.query(Student).filter(Student.student_id==id).first()
    if not student:
        raise HTTPException(
            status_code=404,
            detail=f"Student for id:{id} not found..."
        )
    else:
        return {
            "Student":student
        }
    
@app.put("/update_student/{s_id}")
def update_student(s_id:int,s_name:str,roll:str,db:Session=Depends(get_db)):
    student = db.query(Student).filter(Student.student_id == s_id).first()
    if not student:
        raise HTTPException(
            status_code=404,
            detail=f"No student on id:{id}"
        )
    student.student_name=s_name
    student.student_roll_no=roll
    db.commit()
    all = db.query(Student).all()
    return {
        "status":"Successfully Updated...",
        "Students":all
    }



