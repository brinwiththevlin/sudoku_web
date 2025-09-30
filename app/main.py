"""FastAPI handlers."""

# app/main.py
from fastapi import FastAPI

# Create the FastAPI app instance
app = FastAPI(
    title="Sudoku API",
    description="API for the Sudoku web application.",
    version="1.0.0",
)


# A simple root endpoint to check if the API is running
@app.get("/")
def read_root() -> dict[str, str]:
    """Root Path handler.

    prints a welcom message
    """
    return {"message": "Welcome to the Sudoku API!"}


# In the future, you will include your routers here
# from app.routers import users, puzzles
#
# app.include_router(users.router)
# app.include_router(puzzles.router)
