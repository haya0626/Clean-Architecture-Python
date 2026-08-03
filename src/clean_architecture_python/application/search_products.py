from datetime import datetime
from xxlimited import Str
from zoneinfo import ZoneInfo

from clean_architecture_python.dto.product_dto import ProductDto

"""UseCase"""


class SearchProductsUseCase:
    async def execute(
        self,
        product_name: Str | None,
    ) -> list[ProductDto]:
        """商品を検索し、レスポンス用DTOへ変換する。"""

        normalized_name = (
            # 前後にある空白や改行を削除
            product_name.strip() if product_name else None
        )

        products = await self._product_repository.search(normalized_name)

        APPLICATION_TIMEZONE = ZoneInfo("Asia/Tokyo")

        current_date = datetime.now(tz=APPLICATION_TIMEZONE).date()

        return [ProductDto.from_domain(product, current_date) for product in products]
