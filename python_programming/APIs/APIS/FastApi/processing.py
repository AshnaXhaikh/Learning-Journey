from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Optional
import uvicorn


app = FastAPI(
    title="Simple Text Processing API",
    description="This API provides simple text processing functionalities.",
    version="1.0.0"
)

# Model for text input
class TextRequest(BaseModel):
    text: str
    uppercase: Optional[bool] = False

# Model for text response
class TextResponse(BaseModel):
    processed_text: str
    text_length: int

@app.get("/")  # Root endpoint
def read_root():  # Home endpoint   
    return {"message": "Welcome to the Text Processing API!"}

# Endpoint for text processing
@app.post("/process-text", response_model=TextResponse)
def process_text(request: TextRequest):
    """
    Process the input text based on the request parameters.
    If 'uppercase' is True, convert text to uppercase.
    """
    if not request.text:
        raise HTTPException(status_code=400, detail="Text cannot be empty")

    processed_text = request.text.upper() if request.uppercase else request.text
    return TextResponse(
        processed_text=processed_text, 
        text_length=len(processed_text)
        )

if __name__ == "__main__":  # or uvicorn processing:app --reload in terminal
    uvicorn.run("processing:app", host="127.0.0.1", port=8000, reload=True) 
# This code defines a FastAPI application with a root endpoint and a text processing endpoint.
# The root endpoint returns a welcome message, and the text processing endpoint processes the input text based on the request parameters.
