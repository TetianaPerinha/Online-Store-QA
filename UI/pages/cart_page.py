from .base_page import BasePage
from .locators import CartPageLocators, BasePageLocators

import re


class CartPage(BasePage):
    def click_minus_button(self):
        button = self.browser.find_element(*CartPageLocators.MINUS_BUTTON)
        button.click()

    def click_minus_2_button(self):
        button = self.browser.find_element(*CartPageLocators.MINUS_2_BUTTON)
        button.click()

    def click_plus_button(self):
        button = self.browser.find_element(*CartPageLocators.PLUS_BUTTON)
        button.click()

    def click_plus_2_button(self):
        button = self.browser.find_element(*CartPageLocators.PLUS_2_BUTTON)
        button.click()

    def get_product_cost(self):
        return self.browser.find_element(*CartPageLocators.PRODUCT_COST).text
    
    def get_product_2_cost(self):
        return self.browser.find_element(*CartPageLocators.PRODUCT_2_COST).text

    def get_product_weight(self):
        product_weight_element = self.browser.find_element(*CartPageLocators.PRODUCT_WEIGHT).text
        pattern = re.compile(r'\b\d+\b')
        product_weight = pattern.findall(product_weight_element)
        return product_weight[0]
    
    def get_subtotal(self):
        return self.browser.find_element(*CartPageLocators.SUBTOTAL).text

    def go_to_main_page(self):
        button = self.browser.find_element(*CartPageLocators.CONTINUE_SHOPPING_BUTTON)
        button.click()

    def is_cart_empty(self):
        self.is_element_present(*CartPageLocators.EMPTY_CART_MESSAGE)
    
    # check that amount changed after click "Plus" or "Minus"
    def is_change_amount(self, amount):
        amount_element = self.browser.find_element(*CartPageLocators.AMOUNT)
        if amount_element.text == amount:
            return True
        else: 
            return False
    
    # check that amount on cart icon changed after click "Plus" or "Minus"
    def is_change_cart_icon(self, amount):
        cart_icon = self.browser.find_element(*BasePageLocators.CART_ICON)
        if cart_icon.text == amount:
            return True
        else: 
            return False
    
    # check that product name on main page equal product name on cart page
    def is_product_in_cart(self, main_page_product_name):
        cart_page_product_name = self.browser.find_element(*CartPageLocators.PRODUCT_NAME)
        if cart_page_product_name.text == main_page_product_name:
            return True
        else:
            return False

    def remove_products(self):
        buttons = self.browser.find_elements(*CartPageLocators.REMOVE_BUTTON)
        for button in buttons:
            button.click()
