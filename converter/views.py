from rest_framework.views import APIView
from rest_framework.response import Response
from converter.converter_classes import ConvertCurrencyClass

class CurrencyConverterView(APIView):

   def get(self, request):
        
        try:
            try:
                val1 = request.GET['from']
                val2 = request.GET['to']
                val3 =  request.GET['amount']
            except:
                raise ValueError('Os parâmetros informados não são suficientes.')

            total = ConvertCurrencyClass(val1,val2,val3)

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