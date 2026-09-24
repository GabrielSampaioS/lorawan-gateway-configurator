from selenium.webdriver.common.by import By
from core.page import Page


class NetworkWiFiPage(Page):
    PATH = "/cgi-bin/system-wifi.has"

    WifiName = (
        By.NAME,
        "SSID"
    )

    Passphrase = (
        By.ID, 
        "key"
    )
    SAVE = (
        By.XPATH,
        "//input[@value='Save&Apply']"
    )

    def configure(self, wifiName, passphrase):
        self.open(self.PATH)
        self.fill(self.WifiName, wifiName)
        self.fill(self.Passphrase, passphrase)
        self.save(self.SAVE)