from django.test import TestCase
from rest_framework.test import APIRequestFactory
from rest_framework import status
from ..views import CurrencyConverterView

class BaseModel(TestCase):

    def setUp(self):
        self.data = {
            "from" : "USD",
            "to" : "BRL",
            'amount' : '1'
        }
        self.factory = APIRequestFactory()
        self.view = CurrencyConverterView.as_view()
        

class ViewsetTestCase(BaseModel):

    def test_post_request(self):
        request = self.factory.post('/api/', self.data)
        response = self.view(request)
        self.assertEquals(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)

    def test_get_request(self):
        request = self.factory.get('/api/', self.data)
        response = self.view(request)
        self.assertEquals(response.status_code, status.HTTP_200_OK)

    def test_put_request(self):
        request = self.factory.put('/api/', self.data)
        response = self.view(request)
        self.assertEquals(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)
    
    def test_delete_request(self):
        request = self.factory.delete('/api/', self.data)
        response = self.view(request)
        self.assertEquals(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)

