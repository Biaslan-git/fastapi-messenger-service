from fastapi import FastAPI
from src.auth.router import router as router_auth

app = FastAPI(
    title="Messenger Service"
)

app.include_router(router_auth)

@app.get('/')
async def main():
    return {'message': 'Hello, World!'}
