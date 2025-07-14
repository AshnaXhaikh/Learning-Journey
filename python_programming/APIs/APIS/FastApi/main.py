from fastapi import FastAPI

app = FastAPI(
    title="My FastAPI Application",
    description="This is a sample FastAPI application.",
    version="1.0.0"
)

@app.get("/") # Root endpoint
def read_root(): # Home endpoint                                
    return {"message": "Hello, World!"} # Home message

# greeting endpoint
@app.get("/greet/{name}")
def greet(name: str): # Name parameter
    return {"message": f"Hello, {name}!"} # Greeting message                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            
# @app.get("/items/{item_id}") # Item endpoint
# def read_item(item_id: int, q: str = None): # Query parameter
#     return {"item_id": item_id, "query": q} # Item details with query parameter


if __name__ == "__main__": # or uvicorn main:app --reload in terminal
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000, reload=True)
