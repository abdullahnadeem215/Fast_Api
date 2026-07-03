from fastapi import FastAPI,Depends,Header,HTTPException

app = FastAPI()


def common_logic():
    return {
        "status":"This output is from common_logic function!..."

    }

@app.get("/home")
def home(data = Depends(common_logic)):
    return data


def check_token(token:str = Header(None)):
    if token!= "Hello123":
        raise HTTPException(
            status_code=401,
            detail="Token is not verified!"
        )
    return {
        "status":"Verified!"
    }


@app.get("/secrets")
def secrets(data:str = Depends(check_token)):
    return {
        "status":data
    }