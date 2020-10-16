def calculo_TIEA(TNA,periodo):

    """float,float--> float
    OBJ: Calcular el TIEA
    PRE: periodo>0 y TNA>0"""

    TIEA= (1+(TNA/periodo))**periodo-1

    return TIEA

#PROBADOR1

print(calculo_TIEA(5,3))