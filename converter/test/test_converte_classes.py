from ..converter_classes import ExchangeRequest, CurrencyClass, ConvertCurrencyClass
from django.test import TestCase


class BaseModel(TestCase):

    def setUp(self):

        self.value_from = 'USD'
        self.value_to = 'BRL'
        self.amount = '1'

class ConvertCurrencyClassTestCases(BaseModel):

    def test_return_string(self):
        obj_test = ConvertCurrencyClass(self.value_from, self.value_to, self.amount)
        response = obj_test.get_exchange_value()
        self.assertEquals(str, type(response))

    def test_return_numeric_string(self):
        obj_test = ConvertCurrencyClass(self.value_from, self.value_to, self.amount)
        response = obj_test.get_exchange_value()
        self.assertEquals(float, type(float(response)))

    def test_if_accept_comma_inside_amount_value(self):
        obj_test = ConvertCurrencyClass(self.value_from, self.value_to, '123.23')
        response = obj_test.get_exchange_value()
        self.assertEquals(float, type(float(response)))

    def test_return_excpetion_invalid_from_value(self):
        try:
            obj_test = ConvertCurrencyClass('ABC', self.value_to, self.amount)
            response = obj_test.get_exchange_value()
        except Exception as e:
            self.assertEquals(' ABC não é uma moeda aceita para conversão.', str(e))

    def test_return_excpetion_invalid_to_value(self):
        try:
            obj_test = ConvertCurrencyClass(self.value_from,'DBA', self.amount)
            response = obj_test.get_exchange_value()
        except Exception as e:
            self.assertEquals(' DBA não é uma moeda aceita para conversão.', str(e))
    
    def test_return_excpetion_invalid_amount_value(self):
        try:
            obj_test = ConvertCurrencyClass(self.value_from, self.value_to, 'ABC')
            response = obj_test.get_exchange_value()
        except Exception as e:
            self.assertEquals(' ABC não é um valor válido para conversão.', str(e))
        

class ExchangeRequestTestCases(BaseModel):

    def test_get_values_from_api(self):
        obj_test = ExchangeRequest()
        response = obj_test._get_value_from_api('usd','brl')
        self.assertEquals(float, type(float(response)))

    def test_get_values_from_api_return_exception(self):
        try:
            obj_test = ExchangeRequest()
            response = obj_test._get_value_from_api('TTTT','ADAS')
            self.assertEquals(float, type(float(response)))
        except Exception as e:
            self.assertEquals('API remota não está disponivel.', str(e))


class CurrencyClassTestCases(BaseModel):

    def test_value_validation_true(self):
        obj_test = CurrencyClass()
        response = obj_test.valid_currency_name('USD')
        self.assertEquals('usd', response)

    def test_currency_validation(self):
        obj_test = CurrencyClass()
        response = obj_test.valid_currency_value('5.52')
        response_comma = obj_test.valid_currency_value('5.52')
        self.assertEquals(float('5.52'), response)
        self.assertEquals(float('5.52'), response_comma)

    def test_currency_validation_return_exception(self):
        try:
            obj_test = CurrencyClass()
            response = obj_test.valid_currency_value('ABC')
        except Exception as e:
            self.assertEquals(' ABC não é um valor válido para conversão.', str(e))


    
