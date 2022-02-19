import requests
import json

class ExchangeRequest():
    """ Classe reponsável por realizar requisões na API externa """

    def __init__(self):
        self.__header = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36'}
        self.__url = 'https://cdn.jsdelivr.net/gh/fawazahmed0/currency-api@1/latest/currencies/currency_from/currency_to.json'

    def _get_value_from_api(self,currency_from, currency_to):
        """ Método que irá requisitar a cotação atual da moeda solicitada """
        
        url_aux = self.__url.replace('currency_from', currency_from).replace('currency_to', currency_to)
        page = requests.get(f'{url_aux}', headers=self.__header)

        if page.status_code == 200:
            data = json.loads(page.content.decode('utf-8').replace("'",'"'))
            date,value = data.values()
            return value

        raise Exception('API de consulta não está disponivel.')

class CurrencyClass():
    """ Classe com métodos para validação de parametros relacioados a moeda informada """

    def valid_currency_name(self, value):
        """ Método para validar se a sigla da moeda informada está dentro da relação de moedas 
        que a api pode converter """

        if value.upper() in ["USD","BRL","EUR","BTC","ETH"]:
            return value.lower()
        
        raise ValueError(f" {value} não é uma moeda aceita para conversão.") 
        
    def valid_currency_value(self, value):
        """ Método para validar se o valor informado é realmente um float """

        if type(value) == str:
            value = value.replace(',', '.')
            if value.replace('.','').isnumeric():
                return float(value)
        
        raise ValueError(f" {value} não é um valor válido para conversão.") 

class ConvertCurrencyClass(CurrencyClass,ExchangeRequest):
    """ Classe para converter as moedas passadas por parametro """

    def __init__(self, value_from, value_to, amount):
        super().__init__()
        self.__from_value = self.valid_currency_name(value_from)
        self.__to_value = self.valid_currency_name(value_to)
        self.__rate = self.__get_exchage_rate()
        self.__amount = self.valid_currency_value(amount) 

    def __get_exchage_rate(self):
        """ Método que retona a cotação atual da moeda solicitada """
        return self._get_value_from_api(self.__from_value, self.__to_value)

    def get_exchange_value(self):
        """ Método que retonar o valor da conversão """
        value = self.__amount * self.__rate

        if value < 0.01:
            return "{:.6f}".format(value) 

        return "{:.2f}".format(value) 
