# Organizing Our Bank (Using Routers)

Step 1: Create the Accounts Department (routers/accounts.py)

## Key Changes:
* Use `APIRouter` to create a modular department
* `@app` → `@router` (we're now department-specific)
* All routes automatically get `/accounts` in front
* All routes now start with `/accounts`

The `tags` help `organize documentation`
* `Accounts`: All routes related to account management
* `Transactions`: All routes related to money transactions

* `tags` added to group routes in documentation

```python```python
from fastapi import APIRouter

router = APIRouter()

@router.get("/accounts", tags=["Accounts"])
def get_accounts():
    return {"message": "List of accounts"}

@router.post("/accounts", tags=["Accounts"])
def create_account(account: Account):
    return {"message": "Account created", "account": account}

@router.get("/transactions", tags=["Transactions"])
def get_transactions():
    return {"message": "List of transactions"}

@router.post("/transactions", tags=["Transactions"])
def create_transaction(transaction: Transaction):
    return {"message": "Transaction created", "transaction": transaction}
```