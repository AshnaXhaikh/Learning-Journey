from fastapi import APIRouter

router = APIRouter(
    prefix="/accounts",  # All routes here start with /accounts
    tags=["Withdrawals"]    # Groups these in documentation
)

# Withdrawals router for handling account withdrawals
@router.get("/withdraw")
def get_withdrawal_info(account_id: int):
    return {"account_id": account_id, "withdrawal_limit": 5000, "status": "active"}

# Withdrawals handler
@router.post("/withdraw")
def withdraw_money(account_id: int, amount: float):
    if amount <= 0:
        return {"error": "Withdrawal amount must be positive"}
    # Here you would typically check if the account has enough balance
    return {"message": f"${amount} withdrawn from account {account_id}"}