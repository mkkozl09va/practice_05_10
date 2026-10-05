# Задачи пары: раунд 2 — fizzbuzz, раунд 3 — is_prime.

# Вместо ... впишите своё имя, вместо raise NotImplementedError — решение.
# Проверить, что файл запускается без ошибок: python3 tasks.py



def fizzbuzz(n):
    if n%3==0 and n%5==0: return "FizzBuzz"
    elif n%5==0: return "Buzz"
    elif n%3==0: return "Fizz"
    else: return str(n)
    raise NotImplementedError


def is_prime(n):
    if all([n>1 and n%i!=0 for i in range(2,int(n**0.5)+1)]): return True
    else: return False
    raise NotImplementedError
