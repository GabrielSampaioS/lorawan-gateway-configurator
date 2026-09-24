from selenium.webdriver.common.by import By
from core.page import Page


class NetworkCellularPage(Page):
    PATH = "/cgi-bin/system-cellular.has"

    Apn = (
        By.XPATH,
        "//div[@id='apnListContainer']//input[1]"
    )

    Username = (
        By.XPATH,
         "//div[@id='apnListContainer']//input[2]"
    )

    Password = (
            By.XPATH,
            "//div[@id='apnListContainer']//input[3]"
        )

    Pin = (
            By.NAME,
            "PINCODE"
        )

    SAVE = (
        By.XPATH,
        "//input[@value='Save&Apply']"
    )

    def configure(self, apn, username, password, pin):
        self.open(self.PATH)
        self.fill(self.Apn, apn)
        self.fill(self.Username, username)
        self.fill(self.Password, password)
        self.fill(self.Pin, pin)
        self.save(self.SAVE)