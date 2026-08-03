from clean_architecture_python.infrastructure.mock_product_data import ProductRecord
from clean_architecture_python.infrastructure.mock_product_repository import (
    MockProductRepository,
)


def create_record(
    product_id: str,
    product_name: str,
    deleted_at: str | None = None,
) -> ProductRecord:
    return {
        "product_id": product_id,
        "product_name": product_name,
        "price": 1000,
        "stock_quantity": 1,
        "sales_status": "on_sale",
        "sales_start_date": "2020-01-01",
        "sales_end_date": None,
        "deleted_at": deleted_at,
    }


async def test_search_excludes_logically_deleted_records() -> None:
    records = (
        create_record(product_id="P-1", product_name="表示対象"),
        create_record(
            product_id="P-2",
            product_name="削除対象",
            deleted_at="2026-08-01T10:00:00+09:00",
        ),
    )
    repository = MockProductRepository(records)

    products = await repository.search(None)

    assert [product.product_id for product in products] == ["P-1"]


async def test_search_filters_by_partial_product_name() -> None:
    records = (
        create_record(product_id="P-1", product_name="ノートパソコン"),
        create_record(product_id="P-2", product_name="ワイヤレスマウス"),
    )
    repository = MockProductRepository(records)

    products = await repository.search("パソコン")

    assert [product.product_id for product in products] == ["P-1"]


async def test_search_ignores_letter_case() -> None:
    records = (
        create_record(product_id="P-1", product_name="Gaming Mouse"),
        create_record(product_id="P-2", product_name="Office Keyboard"),
    )
    repository = MockProductRepository(records)

    products = await repository.search("GAMING")

    assert [product.product_id for product in products] == ["P-1"]


async def test_search_returns_empty_list_when_nothing_matches() -> None:
    records = (create_record(product_id="P-1", product_name="ノートパソコン"),)
    repository = MockProductRepository(records)

    products = await repository.search("冷蔵庫")

    assert products == []
