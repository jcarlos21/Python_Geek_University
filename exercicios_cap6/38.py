"""
Questão 38
"""
a = 1
b = 1
c = 980
d = 0
while c <= 986:
    b = 500
    while b < 1000:
        a = 500
        while a < 1000:
            if (a**2 + b**2) == c**2 and c != d:
                print(f'{b, a, c} é um terno pitagórico.')
                d = c  # sacada para não termos o caso (4, 3, 5) e (3, 4, 5), que são a mesma coisa!
            a = a + 1
        b = b + 1
    c = c + 1
