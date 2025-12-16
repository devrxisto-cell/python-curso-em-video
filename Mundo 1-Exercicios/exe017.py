import math
ca = float(input("Digite o valor do cateto adjacente : "))
co = float(input("Digite o valor do cateto oposto : "))
h = math.hypot(ca, co)
print("A hipotenusa é {:.2f}".format(h))
