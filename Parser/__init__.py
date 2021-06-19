import requests
from bs4 import BeautifulSoup as Bs


class CovidParser:
    def __init__(self):
        self.session = requests.Session()
        self.session.headers = {
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.150 Safari/537.36'
        }

    def covid_ekb(self):
        response = self.session.get('https://coronavirus-monitor.info/country/russia/sverdlovskaya-oblast/')
        soup = Bs(response.text, 'lxml')
        div = soup.find_all('div', class_='col-md-4 text-center')
        infected = div[0].text.replace('Заражено', 'Заражено ').strip()
        cured = div[1].text.replace('Вылечено', 'Вылечено ').strip()
        death = div[2].text.replace('Погибло', 'Погибло ').strip()
        data_ekb = [infected, cured, death]
        return data_ekb

    def covid_moscow(self):
        response = self.session.get('https://coronavirus-monitor.info/country/russia/moskva/')
        soup = Bs(response.text, 'lxml')
        div = soup.find_all('div', class_='col-md-4 text-center')
        infected = div[0].text.replace('Заражено', 'Заражено ').strip()
        cured = div[1].text.replace('Вылечено', 'Вылечено ').strip()
        death = div[2].text.replace('Погибло', 'Погибло ').strip()
        data_moscow = [infected, cured, death]
        return data_moscow

    def covid_spb(self):
        response = self.session.get('https://coronavirus-monitor.info/country/russia/sankt-peterburg/')
        soup = Bs(response.text, 'lxml')
        div = soup.find_all('div', class_='col-md-4 text-center')
        infected = div[0].text.replace('Заражено', 'Заражено ').strip()
        cured = div[1].text.replace('Вылечено', 'Вылечено ').strip()
        death = div[2].text.replace('Погибло', 'Погибло ').strip()
        data_spb = [infected, cured, death]
        return data_spb

    def covid_global(self):
        response_rus = self.session.get('https://coronavirus-monitor.info/country/russia/')
        soup = Bs(response_rus.text, 'lxml')
        div = soup.find_all('div', class_='col-md-4 text-center')
        infected = div[0].text.replace('Заражено', 'Заражено ').strip()
        cured = div[1].text.replace('Вылечено', 'Вылечено ').strip()
        death = div[2].text.replace('Погибло', 'Погибло ').strip()

        response_world = self.session.get('https://coronavirus-monitor.info/')
        soup_world = Bs(response_world.content, 'lxml')
        div_world = soup_world.find_all('div', class_='info_blk stat_block confirmed')
        infected_world = div_world[0].text.replace('Заражено', 'Заражено ').strip()
        data_world = [infected, cured, death, infected_world]
        return data_world
