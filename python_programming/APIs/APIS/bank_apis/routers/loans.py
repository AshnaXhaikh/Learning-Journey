from fastapi import APIRouter

router = APIRouter(
    prefix="/loans", # All routes here start with /loans
    tags=["Loans"]    # Groups these in documentation
)

# Get loan details
@router.get("/{loan_id}")
def get_loan(loan_id: int):
    return {"loan_id": loan_id, "amount": 1000, "status": "approved"}

# Apply for a new loan
@router.post("/")
def apply_for_loan(loan: dict):
    return {"message": "Loan application submitted!", "loan": loan}

# get loan status
@router.get("/status/{loan_id}")
def check_loan(loan_id: int):
    return {"loan_id": loan_id, "status": "Active"}