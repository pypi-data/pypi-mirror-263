from itertools import cycle


class Rut:
    """Tipo de datos RUT"""

    def __init__(self, numero="0", digito=None):
        if str(numero).find('-') > 0:
            r_ = numero.split('-')
            numero = r_[0].replace('.', '')
            digito = r_[1]
        self.numero = int(numero)
        self.digito = digito if digito is not None else self.calculate_check_digit()

    """
        Devuelve el Rut formateado 12345678-9
        uso: repr(<objeto: Rut>) Rut(<var>).__repr__() 
    """
    def __repr__(self):
        return "{0:,d}-{1}".format(self.numero, self.digito).replace(',', '').replace('.', '')

    """
        Devuelve el Rut formateado 12.345.678-9
        uso str(<objeto: Rut>) Rut(<var>).__str__()
    """
    def __str__(self):
        return "{0:,d}-{1}".format(self.numero, self.digito).replace(',', '.')

    def calculate_check_digit(self):
        """ Calcula el dígito verificador """
        reversed_digits = map(int, reversed(str(self.numero)))
        factors = cycle(range(2, 8))
        sum_of_digits = sum(digit * factor for digit, factor in zip(reversed_digits, factors))
        calculated_digit = (-sum_of_digits) % 11
        return 'K' if calculated_digit == 10 else str(calculated_digit)

    def is_valid(self):
        """ Retorna validez del rut """
        return self.calculate_check_digit() == self.digito
