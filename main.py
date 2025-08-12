# FastAPI ToDo App - main.py
#
# Basic ToDo API using FastAPI with in-memory storage (not persistent).
# For demo/dev only! Swap to a real DB if you need to keep your tasks.

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional

app = FastAPI()

# Simple data model for a todo item
class Todo(BaseModel):
    id: int
    title: str
    description: Optional[str] = None
    completed: bool = False

# Just keeping todos in a list for now (not saved if you restart)
todos: List[Todo] = []

@app.get("/todos", response_model=List[Todo])
def get_todos():
    # List all todos
    return todos

@app.post("/todos", response_model=Todo, status_code=201)
def create_todo(todo: Todo):
    # Make sure we don't add a todo with duplicate ID
    for t in todos:
        if t.id == todo.id:
            raise HTTPException(status_code=400, detail="Todo with this ID already exists.")
    todos.append(todo)
    return todo

@app.get("/todos/{todo_id}", response_model=Todo)
def read_todo(todo_id: int):
    # Get one todo by its ID
    for t in todos:
        if t.id == todo_id:
            return t
    raise HTTPException(status_code=404, detail="Todo not found.")

@app.put("/todos/{todo_id}", response_model=Todo)
def update_todo(todo_id: int, updated_todo: Todo):
    # Update todo (must use the same ID)
    for idx, t in enumerate(todos):
        if t.id == todo_id:
            todos[idx] = updated_todo
            return updated_todo
    raise HTTPException(status_code=404, detail="Todo not found.")

@app.delete("/todos/{todo_id}", status_code=204)
def delete_todo(todo_id: int):
    # Remove todo by its ID
    for idx, t in enumerate(todos):
        if t.id == todo_id:
            todos.pop(idx)
            return
    raise HTTPException(status_code=404, detail="Todo not found.")