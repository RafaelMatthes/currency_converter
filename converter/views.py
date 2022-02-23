from rest_framework.views import APIView
from rest_framework.response import Response
from converter.converter_classes import ConvertCurrencyClass

class CurrencyConverterView(APIView):

   def get(self, request):
        
        try:
            try:
                from_value = request.GET['from']
                to_value = request.GET['to']
                amount_value =  request.GET['amount']
            except:
                raise ValueError('Os parâmetros informados não são suficientes.')

            total = ConvertCurrencyClass(from_value,to_value,amount_value)

            return Response({
                'exchange_result' : {
                    'value' : total.get_exchange_value()
                }
            },status=200)

        except Exception as e:
            return Response({
                    "error": {
                    "reason": str(e),
                }
            }, status=500)