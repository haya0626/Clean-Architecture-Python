from datetime import datetime
from zoneinfo import ZoneInfo

from clean_architecture_python.dto.product_dto import ProductDto


class SearchProductsUseCase:
    def __init__(self, repository) -> None:
        self._repository = repository

    async def execute(
        self,
        product_name: str | None = None,
    ) -> list[ProductDto]:

        normalized_name = product_name.strip() if product_name else None

        products = await self._repository.search(
            product_name=normalized_name,
        )

        current_date = datetime.now(
            tz=ZoneInfo("Asia/Tokyo"),
        ).date()

        return [
            ProductDto.from_domain(
                product=product,
                current_date=current_date,
            )
            for product in products
        ]
