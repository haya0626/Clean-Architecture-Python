from datetime import date

from cleanarchitecture_python.domain.product import Product, SalesStatus
from cleanarchitecture_python.infrastructure.mock_product_data import ProductRecord


class ProductMapper:
    """DB形式のデータをDomainオブジェクトへ変換するMapper。"""

    @staticmethod
    def to_domain(record: ProductRecord) -> Product:

        sales_end_date = record["sales_end_date"]

        return Product(
            product_id=record["product_id"],
            product_name=record["product_name"],
            price=record["price"],
            stock_quantity=record["stock_quantity"],
            sales_status=SalesStatus(record["sales_status"]),
            sales_start_date=date.fromisoformat(record["sales_start_date"]),
            sales_end_date=(
                date.fromisoformat(sales_end_date) if sales_end_date is not None else None
            ),
        )
