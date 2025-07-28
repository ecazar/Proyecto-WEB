# -*- coding: utf-8 -*-
from fastapi import FastAPI
from app.api import user, book, copy, loan, fine
from app.db.session import engine
from app.db.base import Base  
import asyncio

app = FastAPI(title="Sistema de Biblioteca")

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