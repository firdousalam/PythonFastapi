from fastapi import FastAPI, HTTPException, Query, Path
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
def get_product_by_name(
    name: str = Query(
        default=None, min_length=1, max_length=20, description="search product by name"),
    limit: int = Query(
        default=2, ge=1, le=5, description="please provide limit for pagination"),
    offset: int = Query(default=0, ge=0, description="pagination offset")

):
    products = get_products()
    if name:
        needle = name.strip().lower()
        products = [p for p in products if needle in p.get("name", "").lower()]

    if not products:
        raise HTTPException(
            status_code=404, detail=f"Product not found with name={name}")

    products = sorted(products, key=lambda p: p.get("id", 0), reverse=True)
    product_length = len(products)
    products = products[offset:offset+limit]
    return {"total": product_length, "limit": limit, "offset": offset, "products": products}


@app.get("/productsByProductID/{product_id}")
def get_product(product_id: int = Path(..., min=1, max=1000000, description="id must be 10 digit long", example=1234567890)):
    print(f"product_id {product_id}")
    products = get_all_products()
    return [p for p in products if p["id"] == product_id][0]
