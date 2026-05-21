from contextlib import asynccontextmanager
from fastapi import FastAPI
from src.api_server.api_model_services import APIModelServices
from src.api_server.routes import router

@asynccontextmanager
async def lifespan(app: FastAPI):
    # Add any startup logic here
    api_model_services_obj = APIModelServices()
    model = api_model_services_obj.load_model()
    app.state.api_model_services_obj = api_model_services_obj
    app.state.model = model
    yield
    # Add any cleanup logic here

def create_app():
    app = FastAPI(lifespan=lifespan)
    app.include_router(router)  
    return app