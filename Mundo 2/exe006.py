from datetime import date

ano_nascimento = int(input("Digite o ano do nascimento: "))
ano_atual = date.today().year
idade = ano_atual - ano_nascimento

print(f"\nO atleta nasceu no ano de {ano_nascimento}.")
print(f"\nO atleta tem {idade} anos.")

if idade <=9:
    print("Ele pertence a Categoria: MIRIM ...")
elif idade <= 14:
    print("Ele pertence a Categoria: INFANTIL ...")
elif idade <= 19:
    print("Ele pertence a Categoria: JUNIOR ...")
elif idade <= 25:
    print("Ele pertence a Categoria: SÊNIOR ...")
else:
    print("Ele pertence a Categoria: MASTER !!!")