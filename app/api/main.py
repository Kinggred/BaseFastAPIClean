from fastapi import APIRouter, FastAPI
from fastapi.middleware.cors import CORSMiddleware

# I sudgest importing routers like that:
# from app.api.endpoints.{ module } import router as { module }_router

app = FastAPI()

api_router = APIRouter()
# Include needed routers:
# api_router.include_router(module_router, prefix="/module", tags=["module"] )

app.include_router(api_router)

# TODO: Import CORS from global settings
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
