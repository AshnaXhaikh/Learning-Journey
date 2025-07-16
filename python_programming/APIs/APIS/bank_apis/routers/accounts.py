from fastapi import APIRouter

router = APIRouter(
    prefix="/accounts",  # All routes here start with /accounts
    tags=["Accounts"]    # Groups these in documentation
)
# create accounts 
@router.post("/create")
def create_account(name: str, initial_balance: float):
    return {"message": "Account created", "name": name, "initial_balance": initial_balance}

# same balance checker, but now under /accounts
@router.get("/balance/{account_id}")
def check_balance(account_id: int):
    return {"account_id": account_id, "balance": 10000}

# same deposit handler but now under /accounts
@router.post("/deposit")
def deposit_money(account_id: int, amount: float):
    return {"message": f"${amount} deposited to account {account_id}"}

# delete account 
@router.delete("/{account_id}")
def delete_account(account_id: int):
    return {"message": f"Account {account_id} deleted"}