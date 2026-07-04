import sqlite3
from fastapi import FastAPI

app = FastAPI()
connect = sqlite3.connect("data.sql",check_same_thread=False)

cursor = connect.cursor()


cursor.execute("""
CREATE TABLE IF NOT EXISTS todos(
        id INTEGER PRIMERY KEY,
        title TEXT,
        completed TEXT
    )      
""")

connect.commit()

@app.get("/")
def databaseConeect():
    return {
        "status":"Database connected successfully!"
    }