import pytest
from pages.product_page import ProductPage


@pytest.mark.parametrize(
    "link",
    [
        "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    ],
)
def test_guest_can_add_product_to_basket(browser, link):
    page = ProductPage(browser, link)
    page.open()
    product_name = page.get_product_name()
    product_price = page.get_product_price()
    page.add_to_basket()
    page.should_see_success_message(product_name)
    page.should_see_basket_total(product_price)


if __name__ == "__main__":
    pytest.main(["--capture=no"])
