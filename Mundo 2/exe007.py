seg1 = float(input("Digite o primeiro segmento: "))
seg2 = float(input("Digite o segundo segmento: "))
seg3 = float(input("Digite o terceiro segmento: "))

if seg1 < seg2 + seg3 and seg2 < seg1 + seg3 and seg3 < seg1 + seg2:
    print("\nOs segmentos PODEM formar um triângulo!!!")

    if seg1 == seg2 == seg3:
        print("Tipo de triângulo: EQUILÁTERO (todos os lados são iguais)")
    elif seg1 != seg2 and seg2 != seg3 and seg1 != seg3:
        print("Tipo de triângulo: ESCALENO (todos os lados são diferentes)")
    else:
        print("Tipo de triângulo: ISÓSCELES (dois lados iguais)")
else:
    print("\nOs segentos NÃO PODEM formar um triângulo... ")
