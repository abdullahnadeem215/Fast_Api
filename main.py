from fastapi import FastAPI,Request,HTTPException,status
from products import prod
from dtos import item,user_Response


app = FastAPI()


@app.get("/")
def home():
    return "Welcome to Abdullah's API"


@app.get("/products")
def get_all_prod():
    return prod

##path parameters
@app.get("/product/{product_id}", response_model=user_Response,status_code = status.HTTP_200_OK)
def get_product(product_id:int):
    
    for oneProduct in prod:
        if product_id == oneProduct.get("id"):
            return oneProduct
    return {
        "error":"This id has not been Present"
    }

##Query Parameters
@app.get("/product")
def get_product_query(name:str,age:int):
    return f"Hy {name} Your age is {age}"


@app.get("/productbyrequest")
def get_product_ByRequest(request:Request):

    query_params = dict(request.query_params)

    return  f"Hi {query_params.get("name")} your age is {query_params.get("age")}"

@app.post("/add_product",status_code = status.HTTP_201_CREATED)
def add_product(data:item):
    data = data.model_dump()

    prod.append(data)
    return {"status":"Your Prduct Successfully created...","Products": prod}



###update_product
@app.put("/update_product/{product_id}")
def update_product(data:item,product_id:int):
    for index, each in enumerate(prod):
        if each.get("id") == product_id:
            prod[index]=data.model_dump()
            return {"status":"Product updated succcesfully...","updated_Products":prod}
    return {
        "error":"This id has not been Present"
    }



###Delete API


@app.delete("/delete_product/{product_id}")
def delete_product(product_id:int):
    for index, each in  enumerate(prod):
        if each.get("id")==product_id:
            deleted_product = prod.pop(index)
            return {"status": "Product successfully deleted...","deleted_product":deleted_product}




@app.post("/input")
def json_input_handeling(data:dict):
    return {
        "action":"User_created_data",
        "data":data
    }