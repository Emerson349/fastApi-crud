from fastapi import FastAPI, HTTPException
from localRepository import db
from user import User

app = FastAPI()

@app.get("/")
def home():
    return {"msg": "API rodando"}

@app.post("/users")
def add_user(user: User): 
    db.append(user)
    return user

@app.get("/users")
def get_users(): 
    return db

@app.get("/users/{user_id}")
def get_user(user_id: int):
    for user in db:
        if user.id == user_id:
            return user
    raise HTTPException(404, "User not found")

@app.delete("/users/{user_id}")
def delete_user(user_id: int):
    for user in db:
        if user.id == user_id:
            db.remove(user)
            return {"msg": "deleted"}
        
@app.put("/users/{user_id}")
def update_user(user_id: int, new_data: User):
    for i, u in enumerate(db):
        if u.id == user_id:
            updated = new_data.copy(update={"id": user_id})
            db[i] = updated
            return updated
    raise HTTPException(status_code=404, detail="User not found")