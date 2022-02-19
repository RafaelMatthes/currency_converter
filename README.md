# Conversor de Moedas

API conversora de moedas, utilizando cotação atualizada em tempo real, capaz de realizar a conversão entre as seguintes moedas:
    
    USD
    BRL
    EUR
    BTC
    ETH
    
Exemplo de requisição GET:
    
    http://localhost:8000/api/?from=BRL&to=USD&amount=100
    
Exemplo de output:

    {
      "exchange_result": {
        "value": "19.46"
       }
    }
    
    
# Para executar o projeto:

      1 - docker-compose build
      2 - docker-compose up
         
         
        
# Para executar os testes:
  
       1 - docker exec -it currency-django /bin/bash
       2 - coverage run manage.py test
       3 - coverage report -m

      
Obs: o arquivo '.env' não foi adiconado ao '.gitignore' apenas para facilitar a execução do projeto.
