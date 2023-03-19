from fastapi import FastAPI

app = FastAPI()


@revetl_app.get("/")
async def root():
    return {"message": "Hello World"}