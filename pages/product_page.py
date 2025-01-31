from selenium.webdriver.common.by import By
from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):

    def add_to_basket(self):
        add_button = self.browser.find_element(
            *ProductPageLocators.ADD_TO_BASKET_BUTTON
        )
        add_button.click()
        self.solve_quiz_and_get_code()

    def get_product_name(self):
        return self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text

    def get_product_price(self):
        return self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text

    def should_see_success_message(self, product_name):
        success_message = self.browser.find_element(
            *ProductPageLocators.SUCCESS_MESSAGE
        ).text
        template = "{} has been added to your basket."
        message = self.browser.find_element(*ProductPageLocators.SUCCESS_MESSAGE).text
        assert template.format(message) == template.format(
            product_name
        ), f"{product_name} is not in the success message on page {self.url}"

    def should_see_basket_total(self, product_price):
        basket_total = self.browser.find_element(*ProductPageLocators.BASKET_TOTAL).text
        assert product_price in basket_total, "Product price is not in the basket total"
