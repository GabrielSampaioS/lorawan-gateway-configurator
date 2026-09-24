from selenium.webdriver.common.by import By
from core.page import Page


class LoraLoraPage(Page):
    PATH = "/cgi-bin/lora-lora.has"

    FREQUENCY_PLAN = (
        By.ID,
        "gwcfg"
    )
    SAVE = (
        By.XPATH,
        "//input[@value='Save&Apply']"
    )

    def configure(self, freq):
        self.open(self.PATH)
        self.select(self.FREQUENCY_PLAN, freq)
        self.save(self.SAVE)