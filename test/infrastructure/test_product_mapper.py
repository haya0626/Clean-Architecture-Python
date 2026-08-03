from datetime import date

from clean_architecture_python.domain.product import SalesStatus
from clean_architecture_python.infrastructure.mock_product_data import ProductRecord
from clean_architecture_python.infrastructure.product_mapper import ProductMapper


def test_to_domain_converts_record_values_to_domain_types() -> None:
    record: ProductRecord = {
        "product_id": "P-0001",
        "product_name": "変換テスト商品",
        "price": 3000,
        "stock_quantity": 4,
        "sales_status": "on_sale",
        "sales_start_date": "2026-01-01",
        "sales_end_date": "2026-12-31",
        "deleted_at": None,
    }

    product = ProductMapper.to_domain(record)

    assert product.product_id == "P-0001"
    assert product.sales_status is SalesStatus.ON_SALE
    assert product.sales_start_date == date(2026, 1, 1)
    assert product.sales_end_date == date(2026, 12, 31)
