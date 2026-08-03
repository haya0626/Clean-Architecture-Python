from datetime import date

from clean_architecture_python.domain.product import Product, SalesStatus


def create_product(
    sales_status: SalesStatus = SalesStatus.ON_SALE,
    stock_quantity: int = 10,
    sales_start_date: date = date(2026, 1, 1),
    sales_end_date: date | None = None,
) -> Product:
    return Product(
        product_id="P-TEST",
        product_name="テスト商品",
        price=1000,
        stock_quantity=stock_quantity,
        sales_status=sales_status,
        sales_start_date=sales_start_date,
        sales_end_date=sales_end_date,
    )


def test_is_purchasable_returns_true_when_all_conditions_are_met() -> None:
    product = create_product()

    result = product.is_purchasable(date(2026, 8, 4))

    assert result is True


def test_is_purchasable_returns_false_when_sales_are_stopped() -> None:
    product = create_product(sales_status=SalesStatus.STOPPED)

    result = product.is_purchasable(date(2026, 8, 4))

    assert result is False


def test_is_purchasable_returns_false_when_stock_is_zero() -> None:
    product = create_product(stock_quantity=0)

    result = product.is_purchasable(date(2026, 8, 4))

    assert result is False


def test_is_purchasable_returns_false_before_sales_start_date() -> None:
    product = create_product(sales_start_date=date(2026, 9, 1))

    result = product.is_purchasable(date(2026, 8, 4))

    assert result is False


def test_is_purchasable_returns_true_on_sales_end_date() -> None:
    product = create_product(sales_end_date=date(2026, 8, 4))

    result = product.is_purchasable(date(2026, 8, 4))

    assert result is True


def test_is_purchasable_returns_false_after_sales_end_date() -> None:
    product = create_product(sales_end_date=date(2026, 8, 3))

    result = product.is_purchasable(date(2026, 8, 4))

    assert result is False
