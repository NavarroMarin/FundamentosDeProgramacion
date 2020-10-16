def fuerza(masa, aceleracion):
    """
    float--> float, float
    OBJ: Calcular la fuerza
    PRE: masa>=0, acelarion=cualquier valor
    """
    fuerza= masa*aceleracion
    return fuerza


#Probador1

print(fuerza(2,2))