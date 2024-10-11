# Função que gera números de 1 a 100 definido condições como descritas no exercício e convertendo os valores para string
def fizzbuzz(n):
    # Se o valor inserido for divisível por 3 e 5, será retornado 'Fizzbuzz'
    if n % 3 == 0 and n % 5 == 0:
        return "FizzBuzz"
    # Se o valor for divisível apenas por 5, será retornado 'Buzz'
    if n % 5 == 0:
        return "Buzz"
    # Se o valor for divisível apenas por 3, será retornado 'Fizz'
    if n % 3 == 0:
        return "Fizz"
    return str(n)