from typing import TypedDict


class ProductRecord(TypedDict):
    product_id: str
    product_name: str
    price: int
    stock_quantity: int
    sales_status: str
    sales_start_date: str
    sales_end_date: str | None
    deleted_at: str | None


MOCK_PRODUCT_TABLE: tuple[ProductRecord, ...] = (
    {
        "product_id": "P-1001",
        "product_name": "ノートパソコン",
        "price": 120000,
        "stock_quantity": 10,
        "sales_status": "on_sale",
        "sales_start_date": "2020-01-01",
        "sales_end_date": None,
        "deleted_at": None,
    },
    {
        "product_id": "P-1002",
        "product_name": "ワイヤレスマウス",
        "price": 4500,
        "stock_quantity": 0,
        "sales_status": "on_sale",
        "sales_start_date": "2020-01-01",
        "sales_end_date": None,
        "deleted_at": None,
    },
    {
        "product_id": "P-1003",
        "product_name": "メカニカルキーボード",
        "price": 12800,
        "stock_quantity": 5,
        "sales_status": "stopped",
        "sales_start_date": "2020-01-01",
        "sales_end_date": None,
        "deleted_at": None,
    },
    {
        "product_id": "P-1004",
        "product_name": "期間限定モニター",
        "price": 39800,
        "stock_quantity": 3,
        "sales_status": "on_sale",
        "sales_start_date": "2020-01-01",
        "sales_end_date": "2021-12-31",
        "deleted_at": None,
    },
    {
        "product_id": "P-1005",
        "product_name": "削除済みUSBハブ",
        "price": 2980,
        "stock_quantity": 100,
        "sales_status": "on_sale",
        "sales_start_date": "2020-01-01",
        "sales_end_date": None,
        "deleted_at": "2026-07-01T10:00:00+09:00",
    },
    {
        "product_id": "P-1006",
        "product_name": "予約販売Webカメラ",
        "price": 8900,
        "stock_quantity": 2,
        "sales_status": "on_sale",
        "sales_start_date": "2099-01-01",
        "sales_end_date": None,
        "deleted_at": None,
    },
)
