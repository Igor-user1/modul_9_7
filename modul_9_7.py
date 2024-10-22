import math


def is_prime(func):
    def simple_complex(*args):
        sum_numb = func(*args)
        result = 'Простое'
        a = math.fabs(sum_numb)
        is_squart = math.sqrt(a)
        upper_limit = math.ceil(is_squart) + 1
        for del_ in range(2, upper_limit):
            if a % del_ == 0:
                result = 'Составное'
                break
        return result, sum_numb
    return simple_complex


@is_prime
def sum_three(a, b, c):
    return a + b + c


print(sum_three(-10, 3, -10))
