idade = int(input("Digite sua idade: "))
esporte = int(input("Escolha o Esporte (1 - Natação / 2 - Corrida / 3- Ciclismo): "))
match esporte:
    case 1:
        if idade < 10:
            print("Categoria Mirim")
        elif idade <= 14:
            print("Categoria Infantil")
        else:
            print("Categoria Juvenil")
