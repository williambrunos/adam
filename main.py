from scraper.university_scraper import UniversityScraper


def main():
    university_url = 'https://www.ufc.br/calendario-universitario/2023-resol-n-01-cepe-de-02-02-2023'
    scraper = UniversityScraper(university_webpage_url=university_url)
    scraper.scrap_university_page()
    scraper._fetch_webpage()


if __name__ == '__main__':
    main()
