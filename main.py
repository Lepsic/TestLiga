from fastapi import FastAPI
import uvicorn
from app.db.startup import startup as up_database

app = FastAPI()


@app.on_event('startup')
async def startup():
    await up_database()


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}


if __name__ == '__main__':
    uvicorn.run(app, host='127.0.0.1', port=8000)
