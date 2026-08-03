from fastapi import FastAPI
from fastapi.testclient import TestClient

from clean_architecture_python.application.search_products import SearchProductsUseCase
from clean_architecture_python.infrastructure.mock_product_repository import (
    MockProductRepository,
)
from clean_architecture_python.presentation.product_router import create_product_router


def create_test_client() -> TestClient:
    repository = MockProductRepository()
    use_case = SearchProductsUseCase(repository)

    application = FastAPI()
    application.include_router(create_product_router(use_case), prefix="/api/v1")

    return TestClient(application)


def test_search_products_returns_non_deleted_products() -> None:
    client = create_test_client()

    response = client.get("/api/v1/products")

    assert response.status_code == 200
    product_ids = [product["product_id"] for product in response.json()]
    assert product_ids == ["P-1001", "P-1002", "P-1003", "P-1004", "P-1006"]
    assert "P-1005" not in product_ids


def test_search_products_filters_by_product_name() -> None:
    client = create_test_client()

    response = client.get(
        "/api/v1/products",
        params={"product_name": "パソコン"},
    )

    assert response.status_code == 200
    assert response.json() == [
        {
            "product_id": "P-1001",
            "product_name": "ノートパソコン",
            "price": 120000,
            "stock_quantity": 10,
            "sales_status": "on_sale",
            "sales_start_date": "2020-01-01",
            "sales_end_date": None,
            "is_purchasable": True,
        }
    ]


def test_search_products_returns_empty_list_when_nothing_matches() -> None:
    client = create_test_client()

    response = client.get(
        "/api/v1/products",
        params={"product_name": "冷蔵庫"},
    )

    assert response.status_code == 200
    assert response.json() == []
