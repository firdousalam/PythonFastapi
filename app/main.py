from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def home():
    return {"message": "Hellow World Fastapi"}


@app.get("/products/{id}")
def get_products(id: int):
    products = ["laptop", "mobile", "tv", "ipad"]
    return products[id]
