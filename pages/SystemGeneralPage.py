from selenium.webdriver.common.by import By
from core.page import Page


class SystemGeneralPage(Page):
    PATH = "/cgi-bin/system-general.has"

    Password = (
        By.ID,
        "password"
    )

    Time_Zone = (
        By.ID,
        "timezone"
    )
    SAVE = (
        By.XPATH,
        "//input[@value='Save&Apply']"
    )

    def configure(self, password, timeZone):
        self.open(self.PATH)
        self.fill(self.Password, password)
        self.select(self.Time_Zone, timeZone)
        self.save(self.SAVE)