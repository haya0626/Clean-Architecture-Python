from clean_architecture_python.application.product_repository import ProductRepository
from clean_architecture_python.domain.product import Product
from clean_architecture_python.infrastructure.product_mapper import ProductMapper

class MockProductRepository(ProductRepository):

    def __init__(self, records: ProductRecord = MOCK_PRODUCT_TABLE) -> None:
        self._records = records

    async def search(self, product_name: str | None) -> list[Product]:
        """論理削除を除外し、商品名の部分一致検索を行う。"""

        # deleted_at IS NULL に相当。
        target_records = [record for record in self._records if record["deleted_at"] is None]

        if product_name:
            keyword = product_name.casefold()
            # SQLの LIKE '%検索文字%' に相当。
            target_records = [
                record
                for record in target_records
                if keyword in record["product_name"].casefold()
            ]

        return [ProductMapper.to_domain(record) for record in target_records]
