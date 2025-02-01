# FastAPI Shopping Cart API

## 🚀 Overview
This FastAPI application provides a simple **Shopping Cart API** that allows users to:
- **Add items** to a shopping cart
- **Retrieve** cart contents
- **Delete** a cart
- Perform **health checks** for service availability

## ⚙️ Setup Instructions

1. **Clone the Repository:**
   ```bash
   git clone <repository-url>
   cd <repository-folder>
   ```

2. **Install Dependencies:**
   Ensure you have Python 3.7+ installed. Then install FastAPI and Uvicorn:
   ```bash
   pip install fastapi uvicorn
   ```

3. **Run the Server:**
   ```bash
   uvicorn api_assignment:app --reload
   ```
   - The API will be available at `http://127.0.0.1:8000`.

4. **API Documentation:**
   Visit:
   - **Swagger UI:** `http://127.0.0.1:8000/docs`
   - **ReDoc:** `http://127.0.0.1:8000/redoc`

---

## 📡 API Endpoints

### 1️⃣ **Health Check**
- **Endpoint:** `GET /health`
- **Description:** Verifies if the API is running.
- **Response:**
  ```json
  {
    "status": "Health Ok"
  }
  ```

### 2️⃣ **Add Items to Cart**
- **Endpoint:** `POST /cart`
- **Headers:**
  - `api-key: this-is-the-api-key`
- **Request Body:**
  ```json
  {
    "item-name": "Laptop",
    "quantity": 2,
    "price": 1500
  }
  ```
- **Response:**
  ```json
  {
    "cart-id": 1234,
    "1234": [
      {
        "item-name": "Laptop",
        "quantity": 2,
        "price": 1500
      }
    ],
    "status": "success"
  }
  ```

### 3️⃣ **Get Cart Contents**
- **Endpoint:** `GET /cart`
- **Headers:**
  - `api-key: this-is-the-api-key`
- **Query Parameters:**
  - `cart-id=<cart_id>`
- **Example Request:**
  ```bash
  curl -H "api-key: this-is-the-api-key" "http://127.0.0.1:8000/cart?cart-id=1234"
  ```
- **Response:**
  ```json
  {
    "1234": [
      {
        "item-name": "Laptop",
        "quantity": 2,
        "price": 1500
      }
    ],
    "status": "success"
  }
  ```

### 4️⃣ **Delete Cart**
- **Endpoint:** `DELETE /cart`
- **Headers:**
  - `api-key: this-is-the-api-key`
- **Query Parameters:**
  - `cart-id=<cart_id>`
- **Example Request:**
  ```bash
  curl -X DELETE -H "api-key: this-is-the-api-key" "http://127.0.0.1:8000/cart?cart-id=1234"
  ```
- **Response:**
  ```json
  {
    "status": "success"
  }
  ```

---

## 🔐 Authentication
- **API Key Required:** All endpoints (except `/health`) require an API key:
  ```
  api-key: this-is-the-api-key
  ```
- Requests without the API key will receive a `403 Forbidden` response.

---

## ⚠️ Error Handling
- **Missing API Key:**
  ```json
  {
    "status": "failure"
  }
  ```
- **Invalid Cart ID or Request:**
  ```json
  {
    "status": "failure"
  }
  ```

---

## 💡 Future Improvements
- Add user authentication & authorization.
- Implement cart persistence using a database.
- Improve error messages for better debugging.

---

## 📬 Contact
For issues, feel free to open a GitHub issue or reach out via email.

