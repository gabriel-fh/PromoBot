from scraper import Scrapper

promotions = Scrapper().get_promotions()

for promotion in promotions:
    print(promotion)