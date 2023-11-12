import requests
from _helpers.logger import setup_logger
from bs4 import BeautifulSoup

logger = setup_logger()


class UniversityScraper:
    def __init__(self, university_webpage_url: str):
        self._university_webpage_url = university_webpage_url

    def _fetch_webpage(self):
        """
        This method will fetch the HTML of the source web page

        :return: the response of the HTTP GET method on the source url in string format
        """
        try:
            response = requests.get(self._university_webpage_url)
            response.raise_for_status()
            logger.info(f'SUCCESS ACCESSING {self._university_webpage_url}')
            return response.text
        except requests.RequestException as e:
            logger.error(f'ERROR OF BAD CONTENT ON {self._university_webpage_url}')
            return None

    def scrap_university_page(self):
        """
        This method will scrap the data from the source university url

        :return: webpage data in string format
        """
        page_content = self._fetch_webpage()

        if page_content:
            soup = BeautifulSoup(page_content, 'html.parser')
            university_name = soup.find('h1').text.strip()
            logger.info(f'UNIVERSITY NAME {university_name}')

            months = soup.find_all('h3')
            logger.info(f'MONTHS {months}')

            data = []

            for month in months:
                month_name = month.text.strip()
                data.append(f'\n{month_name}\n')
                logger.info(f'MONTH NAME {month_name}')

                table = month.find_next('table', {'class': 'category'})
                if table:
                    rows = table.find('tbody', {'class': 'listras'}).find_all('tr')

                    for row in rows:
                        day = row.find('td', {'class': 'cell'})
                        day_description = day.find_next('td', {'class': 'cell'})

                        if day and day_description:
                            day_text = day.text.strip()
                            day_description_text = day_description.text.strip()
                            data.append(f'{day_text}: {day_description_text}\n')
                            logger.info(f'{day_text}: {day_description_text}')
                        else:
                            logger.warning(f'INVALID ROW STRUCTURE, SKIPPING')

            with open('data.txt', 'w', encoding='utf-8') as file:
                file.write(''.join(data))
        else:
            logger.error(f'ERROR FETCHING {self._university_webpage_url}')