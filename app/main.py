from fastapi import FastAPI, HTTPException, Query
from service.products import get_all_products

app = FastAPI()


@app.get("/")
def home():
    return {"message": "Hellow World Fastapi"}


@app.get("/products/")
def get_products():
    return get_all_products()


# read data by params
# @app.get("/products/{id}")
# def get_products(id: int):
#     products = ["laptop", "mobile", "tv", "ipad"]
#     return products[id] if products[id] else HTTPException(status_code=403, details="Product not found")

# read data by query
# curl -X 'GET' \
#   'http://127.0.0.1:8000/productsByName?name=tv' \
#   -H 'accept: application/json'
@app.get("/productsByName")
def get_product_by_name(name: str = Query(default=None, min_length=1, max_length=20, description="search product by name")):
    products = get_products()
    if name:
        needle = name.strip().lower()
        products = [p for p in products if needle in p.get("name", "").lower()]

    if not products:
        raise HTTPException(
            status_code=404, detail=f"Product not found with name={name}")

    product_length = len(products)
    return {"total": product_length, "products": products}
