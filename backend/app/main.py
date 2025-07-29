# -*- coding: utf-8 -*-
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api import user, book, copy, loan, fine, auth
from app.db.session import engine
from app.db.base import Base
import asyncio

app = FastAPI(title="Sistema de Biblioteca")


# 🔹 Configurar CORS
origins = [
    "http://localhost:5173",  # Vite/React en desarrollo
    "http://127.0.0.1:5173",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth.router, prefix="/auth", tags=["auth"])
app.include_router(user.router, prefix="/usuarios", tags=["Usuarios"])
app.include_router(book.router, prefix="/libros", tags=["Libros"])
app.include_router(copy.router, prefix="/ejemplares", tags=["Ejemplares"])
app.include_router(loan.router, prefix="/prestamos", tags=["Prestamos"])
app.include_router(fine.router, prefix="/multas", tags=["Multas"])

@app.get("/")
async def root():
    return {"message": "API Biblioteca funcionando"}




@app.on_event("startup")
async def on_startup():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)