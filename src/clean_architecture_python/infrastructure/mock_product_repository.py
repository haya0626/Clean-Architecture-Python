from clean_architecture_python.domain.product import Product
from clean_architecture_python.infrastructure.mock_product_data import (
    MOCK_PRODUCT_TABLE,
    ProductRecord,
)
from clean_architecture_python.infrastructure.product_mapper import ProductMapper


class MockProductRepository:
    def __init__(
        self,
        records: tuple[ProductRecord, ...] = MOCK_PRODUCT_TABLE,
    ) -> None:
        self._records = records

    async def search(self, product_name: str | None) -> list[Product]:
        """論理削除を除外し、商品名の部分一致検索を行う。"""

        # 論理削除済みのデータを除外
        target_records = [record for record in self._records if record["deleted_at"] is None]

        if product_name:
            keyword = product_name.casefold()
            # 部分一致検索
            target_records = [
                record for record in target_records if keyword in record["product_name"].casefold()
            ]

        return [ProductMapper.to_domain(record) for record in target_records]
