fastapi-expenses/
├── main.py
├── models.py
├── requirements.txt
├── expenses.jsonl   ← auto-created on first run
└── README.md

⚙️ Requirements

Python 3.9+

pip (Python package manager)

🚀 Setup Instructions

1️⃣ Clone or create the project folder

cd expenses

2️⃣ Create and activate a virtual environment (recommended)

# Create virtual environment
python -m venv venv

# Activate it
# On macOS/Linux:
source venv/bin/activate

# On Windows:
venv\Scripts\activate

3️⃣ Install dependencies

pip install -r requirements.txt

If you get an “externally-managed-environment” error, either:

pip install --user -r requirements.txt

▶️ Running the App

uvicorn main:app --reload

Swagger URL

👉 http://127.0.0.1:8000/docs

🧠 API Endpoints

| Method   | Endpoint         | Description                |
| -------- | ---------------- | -------------------------- |
| `GET`    | `/`              | Welcome message            |
| `GET`    | `/expenses`      | List all expenses          |
| `GET`    | `/expenses/{id}` | Get a specific expense     |
| `POST`   | `/expenses`      | Add a new expense          |
| `PUT`    | `/expenses/{id}` | Update an existing expense |
| `DELETE` | `/expenses/{id}` | Delete an expense          |


📄 Example JSON for /expenses POST

{
  "id": 1,
  "description": "Lunch at cafe",
  "amount": 250.50,
  "category": "Food",
  "date": "2025-10-29"
}

💾 Data Storage


