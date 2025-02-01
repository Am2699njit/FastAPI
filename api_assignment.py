import fastapi
import random
from fastapi import FastAPI, Response, Header, Query, Body

app = FastAPI()


apikey = "this-is-the-api-key"

shopping_cart = {}




@app.post("/cart")
def add_cart(response: fastapi.Response, api_key: str = fastapi.Header(...), request=fastapi.Body()):
    if api_key != apikey or not api_key:
        response.status_code = 403
        return {"status": "failure"}
    
    if "price" not in request or "item-name" not in request or "quantity" not in request:
        response.status_code = 400
        return {"status": "failure"}

    cart_id = request.get("cart-id")
    if cart_id is None:
        # Generate a unique random cart_id
        while True:
            cart_id = random.randint(1000, 9999)
            if cart_id not in shopping_cart.keys():
                break
        shopping_cart[cart_id] = []
    else:
        try:
            cart_id = int(cart_id)
        except (TypeError, ValueError):
            response.status_code = 400
            return {"status": "failure"}

    if cart_id not in shopping_cart:
        shopping_cart[cart_id] = []

    if cart_id not in shopping_cart:
        shopping_cart[cart_id] = []

    # Check if the item already exists and update quantity
    for item in shopping_cart[cart_id]:
        if item["item-name"] == request["item-name"]:
            item["quantity"] += request["quantity"]  
            response.status_code = 200
            return {"cart-id": cart_id, "status": "success"}

    # Add a new item to the cart
    shopping_cart[cart_id].append({
        "item-name": request["item-name"],
        "quantity": request["quantity"],
        "price": request["price"]
    })

    response.status_code = 200
    return {
        "cart-id": cart_id,  
        str(cart_id): shopping_cart[cart_id],  
        "status": "success"  
    }


@app.get("/cart")
def get_cart(
    response: Response,
    cart_id: str = Query(None, alias="cart-id"),  # Allow `cart_id` to be None
    api_key: str = Header(None, alias="api-key")
):
    """Retrieve the contents of a cart."""
    # Validate API key
    if not api_key or api_key != apikey:
        response.status_code = 403
        return {"status": "failure"}

    # Check if `cart-id` is missing
    if cart_id is None:
        response.status_code = 400
        return {"status": "failure"}

    # Validate `cart-id` value
    if not cart_id.isdigit():
        response.status_code = 400
        return {"status": "failure"}

    cart_id = int(cart_id)
    if cart_id not in shopping_cart:
        response.status_code = 400
        return {"status": "failure"}

    response.status_code = 200
    return {
        str(cart_id): shopping_cart[cart_id],
        "status": "success"
    }



@app.delete("/cart")
def delete_cart(response: Response, cart_id: int = Query(..., alias="cart-id"), api_key: str = Header(...)):
    """Delete a cart by ID."""
    if api_key != apikey or not api_key:
        response.status_code = 403
        return {"status": "failure"}

    if cart_id in shopping_cart:
        del shopping_cart[cart_id]
        response.status_code = 200 
        return {"status": "success"}

    response.status_code = 400
    return {"status": "failure"}

@app.get("/health")
def health(response: Response):
    """Health Check Endpoint"""
    response.status_code = 200
    return {"status": "Health Ok"}