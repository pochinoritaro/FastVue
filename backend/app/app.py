from typing import Union
import data
from fastapi import FastAPI
import uvicorn

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}

@app.get("/user/{username}")
def read_user(username: str):
    return data.read_userdata(username)

if __name__ == '__main__':
    uvicorn.run(app=app)