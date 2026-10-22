nome = input("Nome: ").title()
prova1 = float(input("Prova 01: ").replace(",","."))
prova2 = float(input("Prova 02: ").replace(",","."))
prova3 = float(input("Prova 03: ").replace(",","."))

media = (prova1 + prova2 + prova3)/3

if media >= 7:
    situacao = "aprovado"
elif media >= 5:
    situacao = "recuperação"
else:
    situacao = "reprovado"

print("\nResultado:")
print(f"Nome: {nome}")
print(f"Prova 01: {prova1:.1f}".replace(".",","))
print(f"Prova 02: {prova2:.1f}".replace(".",","))
print(f"Prova 03: {prova3:.1f}".replace(".",","))
print(f"Média: {media:.1f}".replace(".",","))
print(f"Situação: {situacao.upper()}")

