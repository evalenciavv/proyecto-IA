# src/main.py
from fastapi import FastAPI
from src.routers.usuario_routers import router as usuario_router

app = FastAPI(title="API Usuarios")

app.include_router(usuario_router)
