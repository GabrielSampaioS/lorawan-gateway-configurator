# test/configuration.py

from selenium import webdriver

from pages.LoraLoraPage import LoraLoraPage
from pages.LoRaWANSemtechUDPPage import LoRaWANSemtechUDPPage
from pages.NetworkWiFiPage import NetworkWiFiPage
from pages.NetworkCellularPage import NetworkCellularPage
from pages.SystemGeneralPage import SystemGeneralPage

import config
import time

TIMETOSLEEP  = 2


def main():
    driver = webdriver.Edge()
        
    try:
        base_url = (
            f"http://{config.USERNAME2}:{config.PASSWORD2}"
            f"@{config.GATEWAY_IP}"
        )

        print("Configurando LoRa...")
        lora = LoraLoraPage(driver, base_url)
        lora.configure(config.LORA_FREQUENCY_PLAN)

        time.sleep(TIMETOSLEEP)

        print("Configurando LoRaWAN...")
        lorawan = LoRaWANSemtechUDPPage(driver, base_url)
        lorawan.configure(
            config.LORAWAN_EMAIL,
            config.LORAWAN_SERVER
        )

        time.sleep(TIMETOSLEEP)

        print("Configurando Wi-Fi...")
        network_wifi = NetworkWiFiPage(driver, base_url)
        network_wifi.configure(
            config.NETWORKWIFI_WIFI_SSID,
            config.NETWORKWIFI_WIFI_PASSWORD
        )

        time.sleep(TIMETOSLEEP)

        print("Configurando sistema...")
        system_general = SystemGeneralPage(driver, base_url)
        system_general.configure(
            config.SYSTEM_PASSWORD,
            config.SYSTEM_TIMEZONE
        )

        time.sleep(TIMETOSLEEP)

        print("Configurando rede celular...")
        network_cellular = NetworkCellularPage(driver, base_url)
        network_cellular.configure(
            config.NETWORCELLULAR_CELULAR_APN,
            config.NETWORCELLULAR_CELULAR_USERNAME,
            config.NETWORCELLULAR_CELULAR_PASSWORD,
            config.NETWORCELLULAR_CELULAR_PINCORE
        )

        time.sleep(TIMETOSLEEP)

        print("\nConfiguração concluída com sucesso.")

    except Exception as error:
        print(f"\nErro durante a configuração: {error}")
        raise

    finally:
        input("\nPressione Enter para fechar o navegador...")
        driver.quit()


if __name__ == "__main__":
    main()

