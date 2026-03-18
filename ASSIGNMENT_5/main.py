from fastapi import FastAPI

app = FastAPI()

# -----------------------------
# 1. Root Endpoint
# -----------------------------
@app.get("/")
def home():
    return {"message": "Hello World"}


# -----------------------------
# 2. About Endpoint
# -----------------------------
@app.get("/about")
def about():
    return {"info": "This is my FastAPI Assignment"}


# -----------------------------
# 3. Path Parameter
# -----------------------------
@app.get("/user/{user_id}")
def get_user(user_id: int):
    return {"user_id": user_id}


# -----------------------------
# 4. Query Parameter
# -----------------------------
@app.get("/search")
def search(q: str):
    return {"query": q}


# -----------------------------
# 5. Multiple Query Params
# -----------------------------
@app.get("/items")
def get_items(name: str, price: float):
    return {"name": name, "price": price}


# -----------------------------
# 6. POST Request
# -----------------------------
@app.post("/create")
def create_item(name: str, price: float):
    return {
        "message": "Item created",
        "name": name,
        "price": price
    }


# -----------------------------
# 7. PUT Request
# -----------------------------
@app.put("/update/{item_id}")
def update_item(item_id: int, name: str):
    return {
        "message": "Item updated",
        "item_id": item_id,
        "new_name": name
    }


# -----------------------------
# 8. DELETE Request
# -----------------------------
@app.delete("/delete/{item_id}")
def delete_item(item_id: int):
    return {
        "message": "Item deleted",
        "item_id": item_id
    }