from selenium.webdriver.common.by import By
from core.page import Page


class LoRaWANSemtechUDPPage(Page):
    PATH = "/cgi-bin/lorawan.has"

    Email = (
        By.NAME,
        "EMAIL"
    )

    ServerAddress = (
        By.ID, 
        "server_address_ttn_V3"
    )
    SAVE = (
        By.XPATH,
        "//input[@value='Save&Apply']"
    )

    def configure(self, email, serverAddress):
        self.open(self.PATH)
        self.fill(self.Email, email)
        self.select(self.ServerAddress, serverAddress)
        self.save(self.SAVE)