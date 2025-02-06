from fastapi import FastAPI
from app.routes import auth_routes,product_routes
# from app.routes.product_routes import router as product_routes
import uvicorn
from contextlib import asynccontextmanager
from app.Initials.initial_data import preload_sellers

@asynccontextmanager
async def lifespan(app: FastAPI):
    await preload_sellers()  # Perform any startup tasks here
    yield

app = FastAPI(lifespan=lifespan)

app.include_router(auth_routes.router)
app.include_router(product_routes.router)

@app.get("/")
async def root():
    return {"message": "Welcome to the FastAPI MongoDB Project"}

if __name__=="__main__":
    uvicorn.run(app)

