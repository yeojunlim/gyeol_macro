import random
import time
from playwright.sync_api import sync_playwright
from haps import get_haps

URL = "http://localhost:9222"

def main() -> None:
    for i in range(10):
        print(10 - i)
        time.sleep(1)

    with sync_playwright() as p:
        browser = p.chromium.connect_over_cdp(URL)
        page = browser.contexts[0].pages[0]

        hap_btn = page.locator(".call.hap")
        gyeol_btn = page.locator(".call.gyeol")

        while True:
            for hap in get_haps(page.content()):
                try:
                    hap_btn.click()

                    for idx in hap:
                        time.sleep(0.5 + random.random() * 0.5)
                        tile = page.locator(
                            f"//div[contains(@class, 'tile') and ./span[@class='num' and text()='{idx}']]"
                        )
                        tile.click()

                    time.sleep(3 + random.random())
                except Exception as e:
                    print(e)

            gyeol_btn.click()
            time.sleep(3 + random.random())


if __name__ == "__main__":
    main()
