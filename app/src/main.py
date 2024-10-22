from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

from src.auth.router import router as router_auth
from src.pages.router import router as router_pages


app = FastAPI(
    title="Messenger Service"
)

app.mount('/src/static', StaticFiles(directory='src/static'), name='static')

app.include_router(router_auth)
app.include_router(router_pages)
