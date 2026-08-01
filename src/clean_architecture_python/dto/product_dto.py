from dataclasses import dataclass
from datetime import date

from clean_architecture_python.domain.product import Product


@dataclass(frozen=True)
class ProductDto:
    product_id: str
    product_name: str
    price: int
    stock_quantity: int
    sales_status: str
    sales_start_date: date
    sales_end_date: date | None
    is_purchasable: bool

    @classmethod
    def from_domain(cls, product: Product, current_date: date) -> "ProductDto":
        return cls(
            product_id=product.product_id,
            product_name=product.product_name,
            price=product.price,
            stock_quantity=product.stock_quantity,
            sales_status=product.sales_status.value,
            sales_start_date=product.sales_start_date,
            sales_end_date=product.sales_end_date,
            is_purchasable=product.is_purchasable(current_date),
        )
