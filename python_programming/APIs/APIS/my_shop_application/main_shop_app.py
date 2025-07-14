# from fastapi import FastAPI
# from shop_items_router import router as items_router

# # 1. Create the Main Shop Application
# app = FastAPI(
#     title="Shop Application",
#     description="An online shop built with FastAPI.",
#     version="1.0.0"
# )

# # 2. Include the items router
# app.include_router(items_router)

# # 3. Define main shop endpoints
# @app.get("/")  # Root endpoint
# def read_root():
#     return {
#         "message": "Welcome to My Awesome Online Shop API! Check out /items/"
#     }

# @app.get("/about/")
# def about_shop():
#     return {
#         "message": "This is a demo online shop built with FastAPI!"
#     }

from fastapi import FastAPI
from shop_items_router import items_router

# 1. Create the Main Shop Application
app = FastAPI(
    title="Shop Application",
    description="Shop API with Items Router",
    version="1.0.0"
)

# 2. Include the items router
app.include_router(items_router)

# 3. Define main shop endpoints
@app.get("/")
def read_root():
    return {
        "message": "Welcome to My Awesome Online Shop API! Check out /items/"
    }

@app.get("/about/")
def about_shop():
    return {
        "message": "This is a demo online shop built with FastAPI!"
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main_shop_app:app", host="127.0.0.1", port=8000, reload=True)

