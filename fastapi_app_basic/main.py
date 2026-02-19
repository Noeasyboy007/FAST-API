from models import Product
from fastapi import FastAPI
app = FastAPI()


products = [
    Product(id=1, name="Laptop", description="This is a laptop",
            price=1000, quantity=10),
    Product(id=2, name="Mouse", description="This is a mouse",
            price=10, quantity=100),
    Product(id=3, name="Keyboard", description="This is a keyboard",
            price=20, quantity=100),
    Product(id=4, name="Monitor", description="This is a monitor",
            price=30, quantity=100),
    Product(id=5, name="Printer", description="This is a printer",
            price=40, quantity=100),
    Product(id=6, name="Scanner", description="This is a scanner",
            price=50, quantity=100),
    Product(id=7, name="Speaker", description="This is a speaker",
            price=60, quantity=100),
    Product(id=8, name="Headphone", description="This is a headphone",
            price=70, quantity=100),
    Product(id=9, name="Webcam", description="This is a webcam",
            price=80, quantity=100),
    Product(id=10, name="USB Cable",
            description="This is a USB cable", price=90, quantity=100),
]


@app.get("/products")
def get_products():
    return products


@app.get("/products/{product_id}")
def get_product_by_id(product_id: int):
    for product in products:
        if product.id == product_id:
            return product

    return {"error": "Product not found"}


@app.post("/products")
def create_product(product: Product):
    products.append(product)
    return {"message": "Product created successfully"}


@app.put("/products/{product_id}")
def update_product(product_id: int, product: Product):
    for i, p in enumerate(products):
        if p.id == product_id:
            products[i] = product
            return {"message": "Product updated successfully", "product": product}
    return {"error": "Product not found"}


@app.delete("/products/{product_id}")
def delete_product(product_id: int):
    for i, p in enumerate(products):
        if p.id == product_id:
            del products[i]
            return {"message": "Product deleted successfully"}
    return {"error": "Product not found"}
