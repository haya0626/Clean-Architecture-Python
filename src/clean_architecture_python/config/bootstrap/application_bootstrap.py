from fastapi import APIRouter

from clean_architecture_python.config.bootstrap.product_search_api import (
    create_product_search_api_router,
)

""" システムで使用するすべてのAPIをまとめて返す。"""


def create_application_router() -> APIRouter:

    application_router = APIRouter()

    application_router.include_router(
        create_product_search_api_router(),
    )

    # 今後APIを追加する場合は、ここへ登録します。
    #
    # application_router.include_router(
    #     create_order_search_api_router(),
    #     tags=["注文検索"],
    # )
    #
    # application_router.include_router(
    #     create_customer_api_router(),
    #     tags=["顧客"],
    # )

    return application_router
