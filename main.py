def delta(a, b, c):
    return pow(b, 2) - 4 * a * c


def bhaskara(a, b, c):
    resul_delta = delta(a, b, c)

    if resul_delta < 0:
        return 'Delta Negativo'

    raiz_delta = pow(resul_delta, 0.5)

    x1 = (-b + raiz_delta)/(2*a)
    x2 = (-b - raiz_delta)/(2*a)

    return f'x1={round(x1,2)}, x2={round(x2,2)}'

print(bhaskara(7, 3, 4))
# Delta Negativo

print(bhaskara(1, 5, 2))
# x1=-0.44, x2=-4.56

print(bhaskara(3, 10, 2))
# x1=-0.21, x2=-3.12
