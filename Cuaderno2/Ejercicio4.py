def seg_medianoche (h,min,seg):
    """
    int,int,int --> int
    OBJ: Dada una hora,minutos y segundos, calcular los segundos desde la ultima medianoche
    PRE: horas>=0, minutos>=0, segundos>=0

    """
    return h*3600 + min*60 + seg

#Probador1

h=2
min=23
seg=43

print (seg_medianoche(h,min,seg))