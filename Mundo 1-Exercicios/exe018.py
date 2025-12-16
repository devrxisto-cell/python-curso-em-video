import math
entrada = (input("Digite o ângulo que você deseja : "))
entrada = entrada.replace("°", "")
an = float(entrada)
se = math.sin(math.radians(an))
co = math.cos(math.radians(an))
tan = math.tan(math.radians(an))
print("Para o ângulo de {}°, o cosseno é {:.2f}, o seno é {:.2f} e a tangente é {:.2f}. ".format(an, co, se, tan))

