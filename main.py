from fastapi import FastAPI
from src.router import router as wallet_router

app = FastAPI(
    title="Тестовое задание для JavaCode"
)

app.include_router(wallet_router, prefix="/api/v1/wallets")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app)
