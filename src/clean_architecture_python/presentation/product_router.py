from datetime import date
from typing import Annotated

from fastapi import APIRouter
from pydantic import BaseModel

from clean_architecture_python.application.search_products import (
    SearchProductsUseCase,
)
from clean_architecture_python.dto.product_dto import ProductDto


class ProductResponse(BaseModel):
    """商品検索APIのレスポンス。"""

    product_id: str
    product_name: str
    price: int
    stock_quantity: int
    sales_status: str
    sales_start_date: date
    sales_end_date: date | None
    is_purchasable: bool

    @classmethod
    def from_dto(
        cls,
        product_dto: ProductDto,
    ) -> "ProductResponse":
        return cls(
            product_id=product_dto.product_id,
            product_name=product_dto.product_name,
            price=product_dto.price,
            stock_quantity=product_dto.stock_quantity,
            sales_status=product_dto.sales_status,
            sales_start_date=product_dto.sales_start_date,
            sales_end_date=product_dto.sales_end_date,
            is_purchasable=product_dto.is_purchasable,
        )


def create_product_router(
    search_products_use_case: SearchProductsUseCase,
) -> APIRouter:
    """商品検索APIのRouterを作成する。"""

    router = APIRouter(
        prefix="/products",
        tags=["商品検索"],
    )

    @router.get(
        "",
        response_model=list[ProductResponse],
        summary="商品一覧を検索する",
    )
    
    async def search_products() -> list[ProductResponse]:
        product_dtos = await search_products_use_case.execute(
            product_name
        )

        return [
            ProductResponse.from_dto(product_dto)
            for product_dto in product_dtos
        ]

    return router