from fastapi import FastAPI,HTTPException,Depends,Header
from datetime import datetime,timedelta,timezone
from jose import jwt


app = FastAPI()

SECRET = "mysecret"

ALGORITHM = "HS256"

def create_token(data:dict):
    encode = data.copy()
    expire = datetime.now(timezone.utc) + timedelta(minutes=30)

    encode.update({
        "exp":expire
    })

    token = jwt.encode(encode,SECRET,ALGORITHM)
    return token

@app.post("/login")
def login(username:str,password:str):
    if username != "abdullah" or password != "12345":
        raise HTTPException(
            status_code=401,
            detail="Incorrect username or password..."
        )
    token = create_token({
        "user":username
    })
    return {
        "access_token":token
    }

def verify_token(token = Header(None)):
    try:
        payload = jwt.decode(token,SECRET,[ALGORITHM])
        return payload
    except:
        raise HTTPException(
            status_code=401,
            detail="Token is not exist or Expired..."
        )
    
@app.get("/dashboard")
def dashboard(data=Depends(verify_token)):
    return{
        "message":"Successfully LogIn...",
        "data":data
    }