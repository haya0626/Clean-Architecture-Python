from clean_architecture_python.application.product_repository import ProductRepository
from clean_architecture_python.application.search_products import SearchProductsUseCase
from clean_architecture_python.infrastructure.mock_product_repository import (
    MockProductRepository,
)
from clean_architecture_python.presentation.product_router import create_product_router
from fastapi import APIRouter

# Springが自動で行うBean生成とDI等を、Pythonコードで手動実装しているイメージ

"""商品検索APIに必要な依存関係を構築。"""
def create_product_search_api_router(
    product_repository: ProductRepository | None = None,
) -> APIRouter:
    
    repository = MockProductRepository()

    search_products_use_case = SearchProductsUseCase(repository)

    return create_product_router(search_products_use_case)
