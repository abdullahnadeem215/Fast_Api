from fastapi import FastAPI,HTTPException,Depends,Header
from datetime import datetime,timedelta,timezone
from jose import jwt

app = FastAPI()


SECRET_KEY="mysecret"

ALGORITHM = "HS256"

def create_token(data:dict):
    encode = data.copy()
    expire = datetime.now(timezone.utc) + timedelta(minutes=30)

    encode.update({
        "exp":expire
    })

    token = jwt.encode(encode,SECRET_KEY,algorithm=ALGORITHM)

@app.post("/login")
def login(username:str,password:str):
    if username!="abdullah151" or password != "12345":
        raise HTTPException(
            status_code=401,
            detail="Invalid username or password..."
        )
    token = create_token({
        "user":username
    })

    return {
        "token":token
    }