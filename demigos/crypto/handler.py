import requests
import re
from bs4 import BeautifulSoup


class CryptoHandler:
    url = 'https://ru.cryptonator.com/rates/convert/?amount=1&primary={}&secondary={}&source=liverates'

    def get_pair_current_value(self, primary, secondary):
        resp = requests.get(self.url.format(primary, secondary))
        soup = BeautifulSoup(resp.text, 'html.parser')
        results = soup.find_all('strong')
        if results:
            return float(re.findall("\d+\.\d+", results[0].text)[0])
        return None
