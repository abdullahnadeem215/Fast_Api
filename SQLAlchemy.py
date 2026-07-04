from sqlalchemy import create_engine,Column,Integer,String
from sqlalchemy.orm import sessionmaker,declarative_base,Session
from fastapi import FastAPI,Depends


app = FastAPI()

DATABASE_URL = "sqlite:///./data.db"
engine = create_engine(
    DATABASE_URL,
    connect_args={"check_same_thread":False}
)

localSession = sessionmaker(bind=engine)

Base = declarative_base()

class Todos(Base):
    __tablename__="todos"
    id = Column(Integer,primary_key=True,index=True)
    Title = Column(String)
    Completed = Column(String)

Base.metadata.create_all(bind=engine)

def get_db():
    db = localSession()
    try:
        yield db
    finally:
        db.close()

@app.get("/")
def home(session: Session=Depends(get_db)):
    return {
        "status":"Database is Connected Right!"
    }
