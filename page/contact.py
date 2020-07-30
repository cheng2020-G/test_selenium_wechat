from selenium.webdriver.common.by import By

from base.base_page import BasePage
from page.add_member import AddMember


class Contact(BasePage):

    def add_member_contacts(self):
        self.wait_for_click((By.CSS_SELECTOR, ".js_has_member>div:nth-child(1) .js_add_member"))
        self.find(By.CSS_SELECTOR, ".js_has_member>div:nth-child(1) .js_add_member").click()
        return AddMember(self.driver)
