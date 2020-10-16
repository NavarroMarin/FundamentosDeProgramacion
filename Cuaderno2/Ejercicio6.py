def conversor_pintas (ml):
    """
    float-->float
    OBJ: Determinar numero de pintas en cierta cantidad de ml
    PRE: ml>=0
    """
    return ml/473.176473

ml=float(input("Introduzca los mililitros que desea convertir en pintas: "))

print(f"El resultado en pintas es: {conversor_pintas(ml)}")