# 📍 Pincode Lookup API

A simple **FastAPI-based Pincode Lookup API** that provides location information using Indian PIN codes.

The project demonstrates:

* FastAPI REST API development
* Path parameters
* POST request bodies
* Pydantic models
* Pydantic field validation
* Custom exceptions
* Custom exception handlers
* Bulk pincode lookup
* Response models

---

## 🚀 Features

### Single Pincode Lookup

Retrieve location details using a pincode.

```http
GET /pincode/{code}
```

Example:

```http
GET /pincode/411001
```

Response:

```json
{
  "pincode": "411001",
  "city": "Pune",
  "state": "Maharashtra",
  "district": "Pune"
}
```

The API searches the pincode dataset and raises a custom `PinCodeNotFound` exception when the requested pincode does not exist.

---

## 📦 Bulk Pincode Lookup

Look up multiple pincodes in a single request.

```http
POST /pincode/bulk
```

Request body:

```json
{
  "pincodes": [
    "411001",
    "411007",
    "400001"
  ]
}
```

The endpoint separates the requested pincodes into found and missing values and returns the matching location information.

Example response:

```json
{
  "status": "success",
  "found": 3,
  "not_found": 0,
  "missing": [],
  "results": [
    {
      "pincode": "411001",
      "city": "Pune",
      "state": "Maharashtra",
      "district": "Pune"
    },
    {
      "pincode": "411007",
      "city": "Pune",
      "state": "Maharashtra",
      "district": "Pune"
    },
    {
      "pincode": "400001",
      "city": "Mumbai",
      "state": "Maharashtra",
      "district": "Mumbai City"
    }
  ]
}
```

---

## ✅ Validation

The project uses **Pydantic validators** to validate pincode input.

A single pincode must:

* Contain only digits
* Contain exactly 6 digits

Otherwise, validation raises:

```text
Pincode must be a 6-digit number
```

This validation is implemented using Pydantic's `field_validator`.

For bulk requests, the pincode list cannot be empty:

```text
Pincodes list cannot be empty
```

---

## ⚠️ Custom Exception Handling

Instead of directly returning generic errors, the API defines custom exceptions.

### `PinCodeNotFound`

Used when a requested pincode does not exist.

The API returns:

```json
{
  "error": "pincode not found",
  "pincode": "999999"
}
```

with HTTP status:

```http
404 Not Found
```

### `PinCodeError`

A second custom exception is defined for invalid pincodes.

It returns:

```json
{
  "error": "pincode is invalid",
  "pincode": "123",
  "reason": "Invalid pincode"
}
```

with HTTP status:

```http
400 Bad Request
```

The custom exception handlers are registered with FastAPI using:

```python
app.add_exception_handler(
    PinCodeNotFound,
    pincode_not_found_handler
)

app.add_exception_handler(
    PinCodeError,
    invalid_pincode_handler
)
```

---

## 🗂️ Project Structure

```text
PincodeLookup/
│
├── main.py
├── model.py
├── data.py
├── exceptions.py
└── README.md
```

### `main.py`

Contains the FastAPI application and API routes.

```python
app = FastAPI()
```

It contains:

* Home route
* Single pincode lookup
* Bulk pincode lookup
* Exception handler registration

### `model.py`

Contains Pydantic request and response models:

* `PincodeReq`
* `LocationRes`
* `BulkReq`
* `BulkRes`

### `data.py`

Contains the pincode dataset with information such as:

* Pincode
* City
* State
* District

For example, the dataset contains pincodes for Pune, Mumbai, New Delhi, Bengaluru, Chennai, Kolkata, and Jaipur.

### `exceptions.py`

Contains:

* `PinCodeNotFound`
* `PinCodeError`
* `pincode_not_found_handler`
* `invalid_pincode_handler`

---

## 🛠️ Installation

Clone the repository:

```bash
git clone https://github.com/your-username/pincode-lookup-api.git
cd pincode-lookup-api
```

Install the dependencies:

```bash
pip install fastapi uvicorn pydantic
```

---

## ▶️ Running the API

Start the FastAPI development server:

```bash
uvicorn main:app --reload
```

The API will be available at:

```text
http://127.0.0.1:8000
```

---

## 📖 API Documentation

FastAPI automatically provides interactive API documentation.

### Swagger UI

```text
http://127.0.0.1:8000/docs
```

### ReDoc

```text
http://127.0.0.1:8000/redoc
```

---

## 🔗 API Endpoints

| Method | Endpoint          | Description                       |
| ------ | ----------------- | --------------------------------- |
| GET    | `/`               | Welcome message                   |
| GET    | `/pincode/{code}` | Get details for one pincode       |
| POST   | `/pincode/bulk`   | Get details for multiple pincodes |

The root endpoint returns:

```json
{
  "message": "Welcome to Pincode Lookup API"
}
```

---

## 🧪 Example Requests

### Get a Single Pincode

```bash
curl http://127.0.0.1:8000/pincode/411001
```

### Get Multiple Pincodes

```bash
curl -X POST http://127.0.0.1:8000/pincode/bulk \
-H "Content-Type: application/json" \
-d "{\"pincodes\":[\"411001\",\"411007\",\"400001\"]}"
```

---

## 🧠 What This Project Demonstrates

This project is a beginner-friendly example of building a REST API with FastAPI.

The main concepts demonstrated are:

```text
FastAPI
   ↓
Routes
   ↓
Request Models
   ↓
Pydantic Validation
   ↓
Business Logic
   ↓
Custom Exceptions
   ↓
Exception Handlers
   ↓
JSON Response
```

---

## 🔮 Future Improvements

Possible improvements for the project include:

* Move pincodes from an in-memory dictionary to a database
* Add update and delete endpoints
* Add authentication
* Add automated tests with Pytest
* Add Docker support
* Add API versioning
* Add logging
* Add a proper service/repository architecture
* Connect the API to a real pincode database

---

## ⚠️ Current Code Note

There is one type-definition mismatch in the current implementation: `BulkRes.not_found` is declared as `list[str]` in `model.py`, while `main.py` currently passes `len(missing)`, which is an integer.
Before using this as a production API, those two definitions should be made consistent.

---

## 📄 License

This project is intended for learning and educational purposes.
