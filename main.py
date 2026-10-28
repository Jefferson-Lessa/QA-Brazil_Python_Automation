from selenium import webdriver
from selenium.webdriver.chrome.options import Options

import data
import helpers
from pages import UrbanRoutesPage


class TestUrbanRoutes:
    driver = None

    @classmethod
    def setup_class(cls):
        if helpers.is_url_reachable(data.URBAN_ROUTES_URL):
            print("Conectado ao servidor Urban Routes")
        else:
            print("Não foi possível conectar ao Urban Routes. Verifique se o servidor está ligado.")

        options = Options()
        options.set_capability("goog:loggingPrefs", {"performance": "ALL"})
        cls.driver = webdriver.Chrome(options=options)
        cls.driver.maximize_window()

    def setup_method(self):
        self.driver.get(data.URBAN_ROUTES_URL)
        self.routes_page = UrbanRoutesPage(self.driver)

    def _prepare_comfort_order(self):
        self.routes_page.set_route(data.ADDRESS_FROM, data.ADDRESS_TO)
        self.routes_page.click_call_taxi_button()
        self.routes_page.select_comfort_plan()

    def test_set_route(self):
        self.routes_page.set_route(data.ADDRESS_FROM, data.ADDRESS_TO)
        assert self.routes_page.get_from() == data.ADDRESS_FROM
        assert self.routes_page.get_to() == data.ADDRESS_TO

    def test_select_plan(self):
        self._prepare_comfort_order()
        assert self.routes_page.get_current_selected_plan() == 'Comfort'

    def test_fill_phone_number(self):
        self._prepare_comfort_order()
        self.routes_page.set_phone(data.PHONE_NUMBER)
        assert self.routes_page.get_phone() == data.PHONE_NUMBER

    def test_fill_card(self):
        self._prepare_comfort_order()
        self.routes_page.set_card(data.CARD_NUMBER, data.CARD_CODE)
        assert self.routes_page.get_current_payment_method() == 'Cartão'

    def test_comment_for_driver(self):
        self._prepare_comfort_order()
        self.routes_page.set_message_for_driver(data.MESSAGE_FOR_DRIVER)
        assert self.routes_page.get_message_for_driver() == data.MESSAGE_FOR_DRIVER

    def test_order_blanket_and_handkerchiefs(self):
        self._prepare_comfort_order()
        self.routes_page.click_blanket_and_handkerchiefs()
        assert self.routes_page.is_blanket_and_handkerchiefs_selected() is True

    def test_order_2_ice_creams(self):
        self._prepare_comfort_order()
        self.routes_page.add_ice_cream(2)
        assert self.routes_page.get_ice_cream_amount() == 2

    def test_car_search_model_appears(self):
        self._prepare_comfort_order()
        self.routes_page.set_phone(data.PHONE_NUMBER)
        self.routes_page.set_card(data.CARD_NUMBER, data.CARD_CODE)
        self.routes_page.set_message_for_driver(data.MESSAGE_FOR_DRIVER)
        self.routes_page.click_order_taxi_button()
        assert self.routes_page.get_order_popup().is_displayed()

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()
