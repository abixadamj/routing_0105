import uvicorn
from fastapi import FastAPI
from starlette.staticfiles import StaticFiles

from views import komputery
from views import inne
from views import api_responses_test

app = FastAPI()
app.include_router(komputery.router)
app.include_router(inne.router)
app.include_router(api_responses_test.router)
app.mount('/static', StaticFiles(directory='static'), name='static')

@app.get("/")
async def root():
    return {"message": "Hello World"}

if __name__ == '__main__':
    uvicorn.run(app, port=8000, host='127.0.0.1')
