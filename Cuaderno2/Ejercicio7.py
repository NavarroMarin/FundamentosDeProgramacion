def conversor_kelvin(TC):
    """
    float-->float
    OBJ: pasar grados centrigrados a kelvin
    PRE: TC>=-273.15
    """
    return TC+273.15

def conversor_farenhait(TC):
    """
    float-->float
    OBJ: pasar grados centigrados a farenhait
    PRE: TC>=-273.15
    """
    return 9*TC/5+32

TC=float(input("Introduce los grados centigrados que desee: "))

print(f"Los grados centigrados dados son equivalentes a : {conversor_kelvin(TC)} Kelvin y a {conversor_farenhait(TC)} Farenhait")
