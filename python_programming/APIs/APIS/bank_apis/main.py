from fastapi import FastAPI
from routers import accounts, loans, withdrawals

app = FastAPI()

# Include the accounts router
app.include_router(accounts.router)
app.include_router(loans.router)
app.include_router(withdrawals.router)

# greet with user name simple root endpoint
@app.get("/")
def read_root(name: str):
    return {"message": f"Hello, {name}!"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="127.0.0.1", port=8001, reload=True)