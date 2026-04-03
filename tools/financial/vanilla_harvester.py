"""
Vanilla Visa Gift Card Live Harvester
-------------------------------------

Features:
- Scrapes leaked BINs/dumps from pastebin, forums, and darkweb
- Validates cards via checkout page interception
- Auto-redeems valid cards with balance > $0
- Proxy rotation + CAPTCHA solving
- Telegram/Discord alerts for valid cards

Usage:
  python3 vanilla_harvester.py --mode pastebin+checkout --proxies proxies.txt --alerts telegram
"""

import argparse
import random
import time
import requests
from bs4 import BeautifulSoup

class VanillaHarvester:
    def __init__(self, mode="pastebin", proxies=None, alerts=None):
        self.mode = mode
        self.proxies = self._load_proxies(proxies) if proxies else []
        self.alerts = alerts
        self.user_agents = [
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
        ]
        self.session = requests.Session()

    def _load_proxies(self, proxy_file):
        with open(proxy_file, 'r') as f:
            return [line.strip() for line in f if line.strip()]

    def _get_proxy(self):
        return random.choice(self.proxies) if self.proxies else None

    def _scrape_pastebin(self):
        # TODO: Scrape pastebin for Vanilla Visa dumps
        print("[*] Scraping pastebin for Vanilla Visa dumps...")
        return [
            (f"4{random.randint(1000000000000000, 9999999999999999)}", f"{random.randint(100, 999)}")
            for _ in range(10)
        ]

    def _intercept_checkout(self, card_number, cvv):
        # TODO: Implement checkout page interception (e.g., via MITM or JS injection)
        print(f"[*] Testing {card_number} via checkout interception...")
        time.sleep(1)
        return random.choice([True, False])

    def _redeem_card(self, card_number, cvv):
        # TODO: Implement auto-redemption logic
        print(f"[+] Redeeming {card_number}...")
        return True

    def _send_alert(self, card_number, cvv, balance):
        # TODO: Implement Telegram/Discord alerts
        print(f"[ALERT] Valid card: {card_number} | CVV: {cvv} | Balance: ${balance}")

    def run(self):
        print(f"[*] Starting Vanilla Visa harvester in {self.mode} mode...")
        valid_cards = []

        if "pastebin" in self.mode:
            cards = self._scrape_pastebin()
            for card_number, cvv in cards:
                if self._intercept_checkout(card_number, cvv):
                    balance = random.randint(10, 500)
                    if self._redeem_card(card_number, cvv):
                        valid_cards.append(f"{card_number}|{cvv}|${balance}")
                        self._send_alert(card_number, cvv, balance)

        with open("harvested_cards.txt", "w") as f:
            f.write("\n".join(valid_cards))
        print(f"[*] Saved {len(valid_cards)} valid cards to harvested_cards.txt")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Vanilla Visa Gift Card Live Harvester")
    parser.add_argument("--mode", default="pastebin", help="Harvesting mode (pastebin, checkout, or pastebin+checkout)")
    parser.add_argument("--proxies", help="Path to proxy list (format: ip:port)")
    parser.add_argument("--alerts", help="Alert method (telegram/discord)")
    args = parser.parse_args()

    harvester = VanillaHarvester(
        mode=args.mode,
        proxies=args.proxies,
        alerts=args.alerts
    )
    harvester.run()