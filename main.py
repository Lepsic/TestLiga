from fastapi import FastAPI
import uvicorn
from app.db.startup import startup as up_database
from app.endpoints.photo.endpoint import router as photo
from app.endpoints.attribute.endpoint import router as attribute

app = FastAPI()


# @app.on_event('startup')
# async def startup():
#     await up_database()


app.include_router(photo, prefix='/api/photo')
app.include_router(attribute, prefix='/api/attribute')

if __name__ == '__main__':
    uvicorn.run(app, host='127.0.0.1', port=8000)
