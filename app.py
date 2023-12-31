import uvicorn
from fastapi import FastAPI
from router import product, homework
from db import models
from db.database import engine

app = FastAPI(
    title="Homework API",
    description="This API was developed for teaching Fast API",
    version="0.0.1",
    terms_of_service="http://localhost:5000",
)
app.include_router(product.router)
app.include_router(homework.router)


@app.get("/")
def root():
    return {"title": 'HELLO'}


if __name__ == "__main__":
    uvicorn.run("app:app", port=5000, reload=True)


models.Base.metadata.create_all(engine)
