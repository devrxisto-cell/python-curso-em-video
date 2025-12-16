from datetime import date

dia = int(input("Digite o dia do seu nascimento: "))
mes = int(input("Digite o mês do seu nascimento: "))
ano = int(input("Digite o ano do seu nascimento: "))

hoje = date.today()
data_nascimento = date(dia, mes, ano)

idade = hoje.year - data_nascimento.year

if (hoje.month, hoje.day) < (data_nascimento.month, data_nascimento.day):
    idade -= 1

print(f"\nQuem nasceu em {data_nascimento.strftime('%d/%m/%Y')} tem {idade} anos em {hoje.year}.")

if idade < 18:
    saldo = 18 - idade
    ano_alistamento = hoje.year + saldo
    print(f"Ainda faltam {saldo} anos para o alistamento.")
    print(f"Seu alistamento será em {ano_alistamento}.")
elif idade == 18:
    print("Você deve se alistar IMEDIATAMENTE!!!")
else:
    saldo = idade - 18
    ano_alistamento = hoje.year - saldo
    print(f"Você já deveria ter se alistado há {saldo} anos.")
    print(f"Seu alistamento foi em {ano_alistamento}.")
    