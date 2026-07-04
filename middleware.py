from fastapi import FastAPI,Request
import time
app = FastAPI()


# @app.middleware("http")
# async def my_middleware(request:Request,call_next):
#     print("Request Recieved")
    
#     response = await call_next(request)

#     print("Responce sent!")

#     return response


@app.middleware("http")
async def my_middleware(request:Request,call_next):
    start_time = time.time()

    responce = await call_next(Request)

    process_time = time.time()-start_time

    print(f"path:{request.url.path} | Time: {process_time}")

    return responce