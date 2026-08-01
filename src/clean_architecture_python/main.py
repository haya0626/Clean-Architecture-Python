import uvicorn
from fastapi import FastAPI

from clean_architecture_python.config.bootstrap.application_bootstrap import (
    create_application_router,
)
from clean_architecture_python.config.settings import get_settings


def create_app() -> FastAPI:

    settings = get_settings()

    application = FastAPI(
        title=settings.name,
        version="0.1.0",
        description="4層Clean Architectureで実装したAPI",
        docs_url="/docs",
        redoc_url="/redoc",
    )

    application.include_router(
        create_application_router(),
        prefix="/api/v1",
    )

    return application

app = create_app()

def run() -> None:
    # 開発用Webサーバーを起動する。

    settings = get_settings()
    
    uvicorn.run(
       "clean_architecture_python.main:app",
        host=settings.host,
        port=settings.port,
        reload=settings.reload,
    )
