import json
from fastapi import FastAPI, HTTPException
from models import Expense
from pathlib import Path

app = FastAPI(title="Expense Tracker API with JSONL Storage")

DATA_FILE = Path("expenses.jsonl")

def read_expenses():
    """Reads all expenses from the JSONL file"""
    expenses = []
    if DATA_FILE.exists():
        with open(DATA_FILE, "r", encoding="utf-8") as f:
            for line in f:
                expenses.append(json.loads(line.strip()))
    return expenses

def write_expenses(expenses):
    """Writes all expenses back to the JSONL file"""
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        for e in expenses:
            f.write(json.dumps(e) + "\n")

@app.get("/")
def home():
    return {"message": "Welcome to Expense Tracker API"}

@app.get("/expenses")
def get_expenses():
    return read_expenses()

@app.get("/expenses/{expense_id}")
def get_expense(expense_id: int):
    expenses = read_expenses()
    for e in expenses:
        if e["id"] == expense_id:
            return e
    raise HTTPException(status_code=404, detail="Expense not found")

@app.post("/expenses")
def add_expense(expense: Expense):
    expenses = read_expenses()
    # Prevent duplicate IDs
    if any(e["id"] == expense.id for e in expenses):
        raise HTTPException(status_code=400, detail="Expense ID already exists")

    expenses.append(expense.dict())
    write_expenses(expenses)
    return {"message": "Expense added successfully", "expense": expense}

@app.put("/expenses/{expense_id}")
def update_expense(expense_id: int, updated: Expense):
    expenses = read_expenses()
    for i, e in enumerate(expenses):
        if e["id"] == expense_id:
            expenses[i] = updated.dict()
            write_expenses(expenses)
            return {"message": "Expense updated", "expense": updated}
    raise HTTPException(status_code=404, detail="Expense not found")

@app.delete("/expenses/{expense_id}")
def delete_expense(expense_id: int):
    expenses = read_expenses()
    for i, e in enumerate(expenses):
        if e["id"] == expense_id:
            expenses.pop(i)
            write_expenses(expenses)
            return {"message": "Expense deleted"}
    raise HTTPException(status_code=404, detail="Expense not found")
