from fastapi import FastAPI
from .routers import products

app = FastAPI(
    title="CI/CD Demo FastAPI App",
    version="1.0.0"
)

@app.get("/health")
def health_check():
    return {"status": "ok"}

app.include_router(products.router)