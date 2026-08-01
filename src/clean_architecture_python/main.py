import uvicorn
from cleanarchitecture_python.bootstrap.application_bootstrap import (
    create_application_router,
)
from cleanarchitecture_python.config.settings import get_settings
from fastapi import FastAPI
from fastapi.responses import ORJSONResponse


def create_app() -> FastAPI:

    settings = get_settings()

    application = FastAPI(
        title=settings.name,
        version="0.1.0",
        description="4層Clean Architectureで実装したAPI",
        docs_url="/docs",
        redoc_url="/redoc",
        openapi_url="/api/v1/openapi.json",
        default_response_class=ORJSONResponse,
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
        "cleanarchitecture_python.main:app",
        host=settings.host,
        port=settings.port,
        reload=settings.reload,
    )
