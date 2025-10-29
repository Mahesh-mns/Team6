***

# Expenses

A simple expenses tracker API using FastAPI.

```
expenses/
├── main.py
├── models.py
├── requirements.txt
├── expenses.jsonl   ← auto-created on first run
└── README.md
```


***

## Requirements

- Python 3.9+
- pip (Python package manager)

***

## Setup Instructions

1. **Clone or create the project folder**

```sh
cd expenses
```

2. **Create and activate a virtual environment (recommended)**
    - Create virtual environment:

```sh
python -m venv venv
```

    - Activate it:
        - On macOS/Linux:

```sh
source venv/bin/activate
```

        - On Windows:

```sh
venv\Scripts\activate
```

3. **Install dependencies**

```sh
pip install -r requirements.txt
```

*If you get an “externally-managed-environment” error, try:*

```sh
pip install --user -r requirements.txt
```


***

## Running the App

Launch the FastAPI app with:

```sh
uvicorn main:app --reload
```

Access the interactive Swagger UI at:
[http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

***

## API Endpoints

| Method | Endpoint | Description |
| :-- | :-- | :-- |
| GET | `/` | Welcome message |
| GET | `/expenses` | List all expenses |
| GET | `/expenses/{id}` | Get a specific expense |
| POST | `/expenses` | Add a new expense |
| PUT | `/expenses/{id}` | Update an existing expense |
| DELETE | `/expenses/{id}` | Delete an expense |


***

## Example JSON for `/expenses` POST

```json
{
  "id": 1,
  "description": "Lunch at cafe",
  "amount": 250.50,
  "category": "Food",
  "date": "2025-10-29"
}
```


***

## Data Storage

- Expenses are stored in `expenses.jsonl`, which is created automatically on first run.

***

This formatting ensures clarity, improves readability, and provides step-by-step instructions for new users.[^1]

<div align="center">⁂</div>

[^1]: README.md

