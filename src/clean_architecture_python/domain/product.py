from dataclasses import dataclass
from datetime import date
from enum import StrEnum


class SalesStatus(StrEnum):
    """商品の販売状況。"""

    ON_SALE = "on_sale"
    STOPPED = "stopped"


# frozen=True: インスタンス変数の書き換えを防止
@dataclass(frozen=True)
class Product:
    product_id: str
    product_name: str
    price: int
    stock_quantity: int
    sales_status: SalesStatus
    sales_start_date: date
    sales_end_date: date | None

    def is_purchasable(self, current_date: date) -> bool:
        """指定日に商品を購入できるか判定する。

        購入可能条件は次のすべてを満たすこと。
        - 販売中である
        - 在庫が1個以上ある
        - 販売期間内である
        """

        if self.sales_status is not SalesStatus.ON_SALE:
            return False

        if self.stock_quantity < 1:
            return False

        if current_date < self.sales_start_date:
            return False

        return self.sales_end_date is None or current_date <= self.sales_end_date
