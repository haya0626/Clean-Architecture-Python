from datetime import date

from clean_architecture_python.application.product_repository import ProductRepository
from clean_architecture_python.dto.product_dto import ProductDto

"""UseCase"""
class SearchProductsUseCase:
    
    def __init__(
        self,
        product_repository: ProductRepository,
    ) -> None:
        self._product_repository = product_repository

    async def execute(
        self,
        product_name: str | None,
    ) -> list[ProductDto]:
        """商品を検索し、レスポンス用DTOへ変換する。"""

        normalized_name = (
            # 前後にある空白や改行を削除
            product_name.strip()
            if product_name
            else None
        )

        products = await self._product_repository.search(
            normalized_name
        )

        current_date = date.today()

        return [
            ProductDto.from_domain(product, current_date)
            for product in products
        ]