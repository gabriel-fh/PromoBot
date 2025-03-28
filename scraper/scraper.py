import requests
from bs4 import BeautifulSoup


class Scrapper:
    def __init__(self, route=""):
        self.base_url = "https://boletando.com"
        self.route = route  

    def _get_text_or_default(self, element, default=""):
        return element.get_text(strip=True) if element else default

    def _get_attr_or_default(self, element, attr, default=""):
        return element.get(attr, default) if element else default

    def _get_data(self, url):
        try:
            response = requests.get(url)
            response.raise_for_status()
        except requests.exceptions.RequestException as e:
            print(e)
            raise Exception("Ocorreu um erro!: " + str(e))
        return response

    def get_promotions(self):
        url = f"{self.base_url}{self.route}"

        try:
            response = self._get_data(url)
            html = response.text
            soup = BeautifulSoup(html, "html.parser")

            cards = soup.find_all(
                "article",
                class_="col_item offer_grid rehub-sec-smooth offer_grid_com mobile_compact_grid offer_act_enabled",
            )

            products = []

            for card in cards:
                title = card.find("h3")
                price = card.find("span", class_="rh_regular_price")
                payment_method = card.find("span", class_="forma_de_pagamamento")
                link = card.find("a", class_="btn_offer_block")
                image = card.find("figure").find("img")
                coupon = card.find("span", class_="coupon_text")

                product = {
                    "title": self._get_text_or_default(title),
                    "price": self._get_text_or_default(price),
                    "payment_method": self._get_text_or_default(payment_method),
                    "link": self._get_attr_or_default(link, "href"),
                    "image": self._get_attr_or_default(image, "src"),
                    "coupon": self._get_text_or_default(coupon),
                }

                products.append(product)

            return products

        except Exception as e:
            print(e)
            return [{"error": str(e)}]
