from scraper.adam import Adam


def main():
    university_url = 'https://www.ufc.br/calendario-universitario/2024-ajuste-pos-greve'

    scraper = Adam(university_webpage_url=university_url, filename='./data/text/ufc-data-2023')
    scraper.scrap_university_page()


if __name__ == '__main__':
    main()
