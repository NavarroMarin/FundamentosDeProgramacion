import math


def area_circulo(radio):
    """float-->float
    OBJ: Calcula el area de un circulo
    PRE: radio >=0 """
    area = math.pi * radio**2

    return area
print(area_circulo(5))