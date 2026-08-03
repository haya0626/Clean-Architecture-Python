from datetime import date

import pytest

from clean_architecture_python.application.search_products import (
    SearchProductsUseCase,
)
from clean_architecture_python.domain.product import Product, SalesStatus


class FakeProductRepository:
    def __init__(self, products: list[Product]) -> None:
        self.products = products or []
        self.received_name: str | None = None

    async def search(self, product_name: str | None) -> list[Product]:
        self.received_name = product_name
        return self.products


@pytest.mark.parametrize(
    ("input_name", "expected_name"),
    [
        ("  テスト商品\n", "テスト商品"),
        ("   ", None),
        (None, None),
    ],
)
async def test_execute_normalizes_product_name(
    input_name: str | None,
    expected_name: str | None,
) -> None:
    repository = FakeProductRepository([])
    use_case = SearchProductsUseCase(repository)

    await use_case.execute(input_name)

    assert repository.received_name == expected_name


async def test_execute_converts_product_to_dto() -> None:
    product = Product(
        product_id="P-TEST",
        product_name="テスト商品",
        price=1500,
        stock_quantity=2,
        sales_status=SalesStatus.ON_SALE,
        sales_start_date=date(2020, 1, 1),
        sales_end_date=None,
    )

    repository = FakeProductRepository([product])
    use_case = SearchProductsUseCase(repository)

    result = await use_case.execute()

    assert len(result) == 1
    assert result[0].product_id == "P-TEST"
    assert result[0].product_name == "テスト商品"
    assert result[0].sales_status == "on_sale"
    assert result[0].is_purchasable is True
