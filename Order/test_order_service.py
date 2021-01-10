import pytest
from Order.order_service import OrderService, Order

NON_BOOK_TYPE = "Dummy"
BOOK_TYPE = "Book"


def test_only_2_book_orders_in_3_orders_when_sync_book_orders(mocker):
    fake_order_list = create_order_with_specific_type(
        [BOOK_TYPE, BOOK_TYPE, NON_BOOK_TYPE]
    )
    given_fake_order(mocker, fake_order_list)
    mocked_book_dao_insert = mocker.patch("Order.order_service.BookDao.insert")

    order_service = OrderService()
    order_service.sync_book_orders()

    assert mocked_book_dao_insert.call_count == 2
    for i, args in enumerate(mocked_book_dao_insert.call_args_list):
        assert args[0][0] == (fake_order_list[i])


def create_order_with_specific_type(order_type_list):
    return [Order(order_type=order_type) for order_type in order_type_list]


def given_fake_order(mocker, fake_order_list):
    mocker.patch(
        "Order.order_service.OrderService.get_orders",
        return_value=fake_order_list,
    )
