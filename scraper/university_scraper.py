import requests
from _helpers.logger import setup_logger

logger = setup_logger()


class UniversityScraper:
    def __init__(self, university_webpage_url: str):
        self._university_webpage_url = university_webpage_url
        pass

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
            logger.error(f'ERROR FETCHING {self._university_webpage_url}')
            return None

    def scrap_university_page(self):
        """
        This method will scrap the data from the source university url

        :return: webpage data in string format
        """
        pass